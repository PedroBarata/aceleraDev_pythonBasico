import pytest
import requests


class TestStatsAPI:
    # Scope = class, function, module
    @pytest.fixture(scope="class")
    def url(self):
        return "http://localhost:5000/data"

    @pytest.fixture(scope="class")
    def data(self):
        return [1, 2, 3, 4]

    @pytest.fixture(scope="class")
    def uuid(self, url, data):
        response = requests.post(url, json={"data": data})
        return response.json()["uuid"]

    def test_save_data(self, uuid):
        assert uuid is not None

    def test_get_data(self, url, uuid, data):
        response = requests.get(f"{url}/{uuid}")

        assert response.ok
        assert response.json()["data"] == data

    @pytest.mark.parametrize("operation, expected_result", [("mean", pytest.approx(2.5)), ("max", 4), ("min", 1)])
    def test_calc_parameterized(self, url, uuid, operation, expected_result):
        response = requests.get(f"{url}/{uuid}/{operation}")

        assert response.ok
        assert response.json()["result"] == expected_result
