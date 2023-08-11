import pytest
from utils.logger import Logger
from testdata.test_data_generator import TestDataGenerator
from time import sleep
from utils.poll import poll
from utils.common import Common


class TestAsync:
    logger = Logger(__file__).logger

    def setup_method(self, method):
        """Setup method executed before each test method."""
        self.logger.info(f"Setting up for test: {method.__name__}")

    def teardown_method(self, method):
        """Teardown method executed after each test method."""
        self.logger.info(f"Tearing down after test: {method.__name__}")

    @pytest.mark.asynchronous
    def test_sms_sent_flag_update(self, api_request):

        def _sms_sent_flag_updated(id):
            """Inner function to check if the sms_sent flag has been updated to True."""
            response = Common.send_get(api_request, id=id)
            if response.status_code == 200 and response.json().get("sms_sent") == True:
                return True
            return False

        # Step 1: Create a new entry using POST.
        test_data = TestDataGenerator.generate_random_body()
        post_response = api_request("POST", endpoint="/api", json=test_data)
        assert post_response.status_code == 200, f"Failed to create entry: {post_response.text}"

        # Step 2: Wait for the sms_sent flag to be updated using poll.
        test_id = test_data["id"]
        if not poll(_sms_sent_flag_updated, timeout=20, id=test_id):
            assert False, "sms_sent flag was not updated within expected time"
