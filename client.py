#!/usr/bin/env python
import json
import argparse
import requests

from loguru import logger


def send(data):
    # Preciso transformar a string em json, por isso o "json.loads..."
    response = requests.post("http://localhost:5000/data", json={"data": json.loads(data)})

    return response.json()


def retrieve(uuid):
    response = requests.get(f"http://localhost:5000/data/{uuid}")

    return response.json()


def request_operation(uuid, operation_name):
    response = requests.get(f"http://localhost:5000/data/{uuid}/{operation_name}")

    return response.json()


def main():
    parser = argparse.ArgumentParser(description="Test our API")
    parser.add_argument("--send", action="store_true")
    parser.add_argument("--get", action="store_true")
    parser.add_argument("--calc", action="store_true")
    parser.add_argument("--data", dest="data", type=str)
    parser.add_argument("--uuid", dest="uuid", type=str)
    parser.add_argument("--op", dest="op", type=str)

    args = parser.parse_args()

    if args.send and args.data:
        logger.info(f"Sending data '{args.data}'...")
        response = send(args.data)
        logger.info(f"Response: {response}")
    elif args.get and args.uuid:
        logger.info(f"Getting data using UUID '{args.uuid}'...")
        response = retrieve(args.uuid)
        logger.info(f"Response: {response}")
    elif args.calc and args.uuid and args.op:
        logger.info(f"Requested operation '{args.op}' using UUID '{args.uuid}'...")
        response = request_operation(args.uuid, args.op)
        logger.info(f"Response: {response}")
    else:
        logger.warning("No such action selected")


if __name__ == "__main__":
    main()
