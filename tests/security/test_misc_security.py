import pytest
from utils.common import Common
from testdata.test_data_generator import TestDataGenerator


@pytest.mark.security
class TestMiscSecurity:

    def test_post_with_excessive_data(self, api_request):
        """TC019: POST with excessive data (Buffer overflow test)."""
        # Creating a very long string for buffer overflow attempt
        very_long_string = "A" * 1000000
        customer_data = TestDataGenerator.generate_random_body()
        customer_data['name'] = very_long_string

        response = api_request("POST", "/api", json=customer_data)
        assert response.status_code == 400, f"Unexpected response: {response.text}"

    # For CSRF (TC020), it requires a more complex setup and is better tested with specialized tools like OWASP ZAP.
