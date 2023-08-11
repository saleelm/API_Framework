import pytest
from utils.logger import Logger
from testdata.test_data_generator import TestDataGenerator
from time import sleep
from utils.poll import poll
from utils.common import Common


class TestGET:
    logger = Logger(__file__).logger

    def setup_method(self, method):
        """Setup method executed before each test method."""
        self.logger.info(f"Setting up for test: {method.__name__}")

    def teardown_method(self, method):
        """Teardown method executed after each test method."""
        self.logger.info(f"Tearing down after test: {method.__name__}")

    @pytest.mark.functionality
    def test_invalid_user_agent(self, api_request):
        """Test to verify behavior when an invalid user-agent value is provided."""

        headers = {
            "user-agent": "test-bot"  # This should be considered invalid since it contains the "bot" keyword
        }

        response = Common.send_get(api_request)
        self.logger.info(
            f"Received Response - Status: {response.status_code}, Headers: {response.headers}, Body: {response.text},Request Headers: {response.request.headers}")

        # Expected status code can be adjusted based on the API's behavior for invalid headers.
        assert response.status_code == 400

    @pytest.mark.functionality
    def test_create_and_retrieve_entry(self, api_request):
        """Test to create an entry and then fetch it using its ID."""

        def _customer_exists(id):
            """Inner function to check if a customer exists. Returns True if it does, otherwise False."""
            response = Common.send_get(api_request, id=id)
            return response.status_code == 200

        # Step 1: Create a new entry using POST.
        test_data = TestDataGenerator.generate_random_body()
        post_response = api_request("POST", endpoint="/api", json=test_data)
        self.logger.info(
            f"POST Response - Status: {post_response.status_code}, Headers: {post_response.headers}, Body: {post_response.text},Accessed URL: {post_response.url},Request Headers: {post_response.request.headers}"
        )
        assert post_response.status_code == 200, f"Failed to create entry: {post_response.text}"

        # Step 2: Wait for the customer to be available using poll.
        test_id = test_data["id"]
        if not poll(_customer_exists, timeout=20, id=test_id):
            assert False, "Failed to retrieve customer within expected time"

        # Step 3: Now, retrieve the customer entry since we know it exists.
        get_response = Common.send_get(api_request, id=test_id)
        self.logger.info(
            f"GET Response - Status: {get_response.status_code}, Body: {get_response.text},"
            f"Accessed URL: {get_response.url},Request Headers: {get_response.request.headers}"
        )
        assert get_response.status_code == 200, f"Failed to retrieve entry: {get_response.text}"

        # Ensure the retrieved data matches the posted data.
        retrieved_data = get_response.json()
        assert retrieved_data["id"] == test_data["id"]
        assert retrieved_data["name"] == test_data["name"]
        assert retrieved_data["phone_number"] == test_data["phone_number"]
        assert retrieved_data["sms_sent"] == True
