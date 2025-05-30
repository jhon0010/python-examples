from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 5)  # Simulated delay between tasks (1–5s)

    @task(3)    
    def get_items(self):
        print(self.client.post("/users", json={
            "name": "peter",
            "email": "peter@example.ecommerce.com",
            "password": "mysecurepassword123"
        }
    ))
        
    @task
    def get_users(self):
        print(self.client.get("/users/jhon"))