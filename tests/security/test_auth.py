import pytest
from utils.common import Common
from testdata.test_data_generator import TestDataGenerator
from utils.logger import Logger


@pytest.mark.security
class TestAuthentication:
    logger = Logger(__file__).logger

    def setup_method(self, method):
        """Setup method executed before each test method."""
        self.logger.info(f"Setting up for test: {method.__name__}")

    def teardown_method(self, method):
        """Teardown method executed after each test method."""
        self.logger.info(f"Tearing down after test: {method.__name__}")

    def test_post_without_session_token(self, api_request):
        """TC014: POST without x-session-token header."""
        customer_data = TestDataGenerator.generate_random_body()

        # Simulating the absence of x-session-token header
        headers = {
            "x-session-token": None
        }

        response = api_request("POST", "/api", json=customer_data, headers=headers)
        assert response.status_code == 403, f"Unexpected response: {response.text}"

    def test_post_with_bot_user_agent(self, api_request):
        """TC015: POST with user-agent containing 'bot'."""
        customer_data = TestDataGenerator.generate_random_body()

        headers = {
            "user-agent": "test_bot"
        }
        response = Common.send_post(api_request, payload=customer_data, headers=headers)
        self.logger.info(
            f"POST Response - Status: {response.status_code}, Headers: {response.headers}, Body: {response.text},Accessed URL: {response.url},Request Headers: {response.request.headers}")
        assert response.status_code == 400, f"Unexpected response: {response.text}"


    def test_brute_force_session_token(self, api_request):
        """TC017: Brute force x-session-token."""
        # Simulating brute force by sending multiple requests in a short period. (Note: This is a simple representation, real brute force will require more advanced setup)
        for _ in range(10):
            customer_data = TestDataGenerator.generate_random_body()
            response = api_request("POST", "/api", json=customer_data)
            assert response.status_code in [401,
                                            429], f"Unexpected response: {response.text}"  # 429 is for Too Many Requests
