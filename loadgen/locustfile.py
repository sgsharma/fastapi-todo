import uuid
from locust import HttpUser, task, constant

class MyUser(HttpUser):
    wait_time = constant(6)  # 10 requests per minute, 60 seconds / 10 requests = 6 seconds

    @task
    def create_entry(self):
        todoid = str(uuid.uuid4())
        # Increment the title counter for each request
        title = f"Test Entry {todoid}"

        entry_data = {
            "entry": title
        }

        # Make a POST request to create an entry
        self.client.post("/api/v1/entries/", json=entry_data)
