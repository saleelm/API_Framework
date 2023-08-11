class Common:

    @staticmethod
    def send_get(api_request, id=None,**kwargs):
        """Helper function to send GET request."""
        endpoint = "/api"
        if id:
            endpoint += f"?id={id}"
        return api_request("GET", endpoint)

    @staticmethod
    def send_post(api_request, payload,**kwargs):
        """Helper function to send POST request."""
        endpoint = "/api"
        return api_request("POST", endpoint, json=payload,**kwargs)
