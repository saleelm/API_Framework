import pytest
from utils.common import Common
from utils.logger import  Logger
from testdata.test_data_generator import TestDataGenerator


@pytest.mark.datatype
class TestStringValidation:
    logger = Logger(__file__).logger

    def setup_method(self, method):
        """Setup method executed before each test method."""
        self.logger.info(f"Setting up for test: {method.__name__}")

    def teardown_method(self, method):
        """Teardown method executed after each test method."""
        self.logger.info(f"Tearing down after test: {method.__name__}")

    def test_string_in_phone_number(self, api_request):
        """TC025: Test POST with string value in phone_number."""
        customer_data = TestDataGenerator.generate_body_with_string_phone()
        response = Common.send_post(api_request, customer_data)
        assert response.status_code == 400, f"Unexpected response: {response.text}"

    def test_post_with_max_values(self, api_request):
        """TC028: POST with max allowed size/values."""
        customer_data = TestDataGenerator.generate_body_with_max_values()
        response = Common.send_post(api_request, customer_data)
        assert response.status_code == 500, f"Unexpected response: {response.text}"

    def test_non_english_characters_in_name(self, api_request):
        """TC029: Test POST with non-English characters in name."""
        customer_data = TestDataGenerator.generate_body_with_non_english_name()
        response = Common.send_post(api_request, customer_data)
        assert response.status_code == 400, f"Unexpected response: {response.text}"
