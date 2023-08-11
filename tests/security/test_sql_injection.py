import pytest
from utils.common import Common


@pytest.mark.security
class TestSQLInjection:

    def test_sql_injection_in_id_field(self, api_request):
        """TC016: Attempt SQL injection in id field."""
        # Using a typical SQL injection string.
        injection_string = "1' OR '1' = '1'; --"

        response = Common.send_get(api_request,id=injection_string)
        assert response.status_code in [400, 500], f"Unexpected response: {response.text}"
