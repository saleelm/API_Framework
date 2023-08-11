from locust import HttpUser, task, between
from testdata.test_data_generator import TestDataGenerator
from utils.logger import Logger


class PerformanceTest(HttpUser):
    host = "http://localhost:8080"
    wait_time = between(1, 3)
    logger = Logger(__file__).logger

    @task
    def load_test(self):
        test_data = TestDataGenerator.generate_random_body()
        headers = {
            "x-session-token": "authorized-user",
            "user-agent": "test",
            "Content-Type": "application/json"
        }
        # Use Locust's client to make the request
        response = self.client.post("/api", json=test_data,headers=headers)

        # Assert the response code
        assert response.status_code == 200, f"Failed load test request! Status code: {response.status_code}, Response: {response.text}"

    @task
    def spike_test(self):
        test_data = TestDataGenerator.generate_random_body()
        headers = {
            "x-session-token": "authorized-user",
            "user-agent": "test",
            "Content-Type": "application/json"
        }
        for _ in range(100):  # Simulating sudden spike
            response = self.client.post("/api", json=test_data,headers=headers)

            self.logger.info(
                f"Spike Test Response - Status: {response.status_code}, Headers: {response.headers}, Body: {response.text}"
            )

            assert response.status_code == 200, "Failed spike test request!"
