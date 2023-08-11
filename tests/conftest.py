import pytest
import requests
from utils.logger import  Logger

BASE_URL = "http://localhost:8080"



@pytest.fixture
def api_request():
    def _request(method, endpoint, **kwargs):
        # Default headers
        headers = {
            "x-session-token": "authorized-user",
            "user-agent": "test",
            "Content-Type":"application/json"
        }

        # If there are any headers in kwargs, update the default headers with them
        headers.update(kwargs.get("headers", {}))

        # Assign updated headers back to kwargs
        kwargs["headers"] = headers

        # Construct full URL
        full_url = f"{BASE_URL}{endpoint}"
        print(full_url)

        return requests.request(method, full_url, **kwargs)

    return _request
