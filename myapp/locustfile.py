from locust import HttpUser, task


class RequestUser(HttpUser):
    @task
    def request(self):
        self.client.get('/')
        self.client.get('/detail')
