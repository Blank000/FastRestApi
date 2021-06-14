import sys

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


class TestApp:

    # Testing 'http://127.0.0.1:8000/sum' endpoint with various inputs

    def test_update_item(self):
        response = client.put("/sum", json={"values": [1, 2, 3]})
        assert response.status_code == 200
        assert response.json() == {"status": 200, "result": 6}

        response = client.put("/sum", json={"values": [2, 13, 1]})
        assert response.status_code == 200
        assert response.json() == {"status": 200, "result": 3}

        response = client.put("/sum", json={"values": [2, 1, 14]})
        assert response.status_code == 200
        assert response.json() == {"status": 200, "result": 3}

        response = client.put("/sum", json={"values": [2, 1, 15]})
        assert response.status_code == 200
        assert response.json() == {"status": 200, "result": 18}

        response = client.put("/sum", json={"values": [1, 2]})
        assert response.status_code == 400
        assert response.json() == {"status": 400, "error": "Exactly 3 numbers are required"}

        response = client.put("/sum", json={"values": [1, 2, "a"]})
        assert response.status_code == 400
        assert response.json() == {"status": 400, "error": "All inputs must be numeric"}