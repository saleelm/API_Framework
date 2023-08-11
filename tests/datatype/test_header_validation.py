import pytest
from utils.common import Common
from utils.logger import Logger
from testdata.test_data_generator import TestDataGenerator


@pytest.mark.datatype
class TestHeaderValidation:
    logger = Logger(__file__).logger

    def setup_method(self, method):
        """Setup method executed before each test method."""
        self.logger.info(f"Setting up for test: {method.__name__}")

    def teardown_method(self, method):
        """Teardown method executed after each test method."""
        self.logger.info(f"Tearing down after test: {method.__name__}")

    def test_post_with_missing_headers(self, api_request):
        """TC027: POST with missing headers."""
        customer_data = TestDataGenerator.generate_random_body()

        # To simulate missing headers, remove the headers in the API request.
        # Using a dictionary to remove the "x-session-token" header.
        headers = {
            "x-session-token": None
        }

        response = api_request("POST", "/api", json=customer_data, headers=headers)
        assert response.status_code == 403, f"Unexpected response: {response.text}"

    # You can add more header validation tests as needed.
