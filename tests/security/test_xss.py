import pytest
from utils.common import Common

@pytest.mark.security
class TestXSS:

    def test_xss_in_name_field(self, api_request):
        """TC018: Attempt XSS in name field."""
        xss_payload = "<script>alert('XSS');</script>"

        # Send post request with xss payload in the name field.
        data = {
            "id": "1234567890123",
            "name": xss_payload,
            "phone_number": "1234567890"
        }

        response = Common.send_post(api_request,payload=data)
        assert response.status_code == 400, f"Unexpected response: {response.text}"
