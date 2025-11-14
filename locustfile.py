from locust import HttpUser,task,between

class MyStressTestUser(HttpUser):
    wait_time = between(1,2)

    @task
    def get_posts(self):
        self.client.get('/posts')

    @task
    def create_post(self):
        self.client.post('/posts', json=
                         {"title":"bikramtest", 
                          "body":"testbody",
                          "userId":1})