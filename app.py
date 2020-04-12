#!/usr/bin/env python

from flask import Flask, request, jsonify
from loguru import logger

from statsapi import operation, data_store


app = Flask(__name__)


@app.route("/data", methods=["POST"])
def save_data():
    logger.info(f"Saving data...")
    content = request.get_json()
    uuid = data_store.save(content["data"])
    logger.info(f"Data saved with UUID '{uuid}' successfully!")

    return jsonify({"status": "success", "message": "Data saved", "uuid": uuid})


@app.route("/data/<uuid>", methods=["GET"])
def retrieve_data(uuid):
    logger.info(f"Retrieving data associated with UUID '{uuid}'...")
    try:
        stored_data = data_store.get(uuid)
    except KeyError:
        logger.warning(f"Cannot retrieving data associated with UUID '{uuid}'")
        return jsonify({"status": "failed", "message": "Cannot retrieve data", "data": []})
    logger.info(f"Data associated with UUID '{uuid}' retrieved successfully!")

    return jsonify({"status": "success", "message": "Data retrieved successfully", "data": stored_data})


@app.route("/data/<uuid>/<operation>", methods=["GET"])
def process_operation(uuid, operation):
    logger.info(f"Processing operation '{operation}' on data associated with UUID '{uuid}'...")

    try:
        stored_data = data_store.get(uuid)
        operation_func = get_operation(operation)
        result = operation_func(stored_data)
    except KeyError:
        logger.warning(f"Cannot retrieving data associated with UUID '{uuid}'")
        return jsonify({"status": "failed", "message": "Cannot retrieve data", "result": None})
    except NoSuchOperationError:
        logger.warning(f"Cannot find operation '{operation}'")
        return jsonify({"status": "failed", "message": f"No such '{operation}'", "result": None})

    logger.warning(f"Operation '{operation}' on data associated with UUID '{uuid}' finished successfully!")

    return jsonify({"status": "success", "message": "Result completed", "result": result})


class NoSuchOperationError(Exception):
    pass


def get_operation(operation_name):
    if operation_name == "min":
        return operation.op_min
    if operation_name == "max":
        return operation.op_max
    if operation_name == "mean":
        return operation.op_mean
    else:
        return NoSuchOperationError


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

