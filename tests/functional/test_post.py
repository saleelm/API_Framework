import pytest
from testdata.test_data_generator import TestDataGenerator
from utils.logger import Logger
from utils.common import Common
import json


class TestPOST:
    logger = Logger(__file__).logger

    def setup_method(self, method):
        """Setup method executed before each test method."""
        self.logger.info(f"Setting up for test: {method.__name__}")

    def teardown_method(self, method):
        """Teardown method executed after each test method."""

        self.logger.info(f"Tearing down after test: {method.__name__}")

    @pytest.mark.functional
    def test_post_valid_fields(self, api_request):
        """Test 001 : Post with valid fields."""
        test_data = TestDataGenerator.generate_random_body()
        self.logger.info(json.dumps(test_data))
        response = Common.send_post(api_request, test_data)
        try:
            # Parse the response JSON
            response_content = response.json()

            # Assert the status code and the message
            assert response.status_code == 200
            assert response_content["message"] == "customer created"
        except AssertionError as e:
            self.logger.error(f"Test failed! Reason: {e}")
            raise
        else:
            self.logger.info("Test passed!")

    @pytest.mark.functional
    def test_post_without_id(self, api_request):
        test_data = TestDataGenerator.generate_random_body()
        del test_data["id"]
        response = Common.send_post(api_request, test_data)
        self.logger.info(
            f"Received Response - Status: {response.status_code}, Headers: {response.headers}, Body: {response.text}")
        assert response.status_code == 400

    @pytest.mark.functional
    def test_post_name_exceeding_limit(self, api_request):
        test_data = TestDataGenerator.generate_random_body()
        test_data["name"] = "a" * 51  # 51 characters
        response = Common.send_post(api_request, test_data)
        self.logger.info(
            f"Received Response - Status: {response.status_code}, Headers: {response.headers}, Body: {response.text}")
        assert response.status_code == 500

    @pytest.mark.functional
    def test_post_with_special_characters_in_name(self, api_request):
        test_data = TestDataGenerator.generate_random_body()
        test_data["name"] = "John$Doe"  # Contains a special character
        response = Common.send_post(api_request, test_data)
        self.logger.info(
            f"Received Response - Status: {response.status_code}, Headers: {response.headers}, Body: {response.text}")
        assert response.status_code == 400

    @pytest.mark.functional
    def test_post_phone_number_not_10_chars(self, api_request):
        test_data = TestDataGenerator.generate_random_body()
        test_data["phone_number"] = "12345"  # Only 5 characters
        response = Common.send_post(api_request, test_data)
        self.logger.info(
            f"Received Response - Status: {response.status_code}, Headers: {response.headers}, Body: {response.text}")
        assert response.status_code == 500

    @pytest.mark.functional
    def test_post_empty_name(self, api_request):
        test_data = TestDataGenerator.generate_random_body()
        test_data["name"] = ""
        self.logger.info(test_data)
        response = Common.send_post(api_request, test_data)
        self.logger.info(
            f"Received Response - Status: {response.status_code}, Headers: {response.headers}, Body: {response.text}")
        assert response.status_code == 400

    @pytest.mark.functional
    def test_post_empty_phone_number(self, api_request):
        test_data = TestDataGenerator.generate_random_body()
        test_data["phone_number"] = ""
        response = Common.send_post(api_request, test_data)
        self.logger.info(
            f"Received Response - Status: {response.status_code}, Headers: {response.headers}, Body: {response.text}")
        assert response.status_code == 400

    @pytest.mark.functional
    def test_post_non_numeric_phone_number(self, api_request):
        test_data = TestDataGenerator.generate_random_body()
        test_data["phone_number"] = "abcdefghij"  # Non-numeric
        response = Common.send_post(api_request, test_data)
        self.logger.info(
            f"Received Response - Status: {response.status_code}, Headers: {response.headers}, Body: {response.text}")
        assert response.status_code == 400

    @pytest.mark.functional
    def test_post_duplicate_entry(self, api_request):
        test_data = TestDataGenerator.generate_random_body()
        response1 = Common.send_post(api_request, test_data)
        self.logger.info(
            f"Received Response - Status: {response1.status_code}, Headers: {response1.headers}, Body: {response1.text}")
        response2 = Common.send_post(api_request, test_data)
        self.logger.info(
            f"Received Response - Status: {response2.status_code}, Headers: {response2.headers}, Body: {response2.text}")
        assert response1.status_code == 200
        assert response2.status_code == 400
