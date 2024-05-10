from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)  

    @task
    def index(self):
        self.client.get("/")  

    @task
    def add_student(self):
        self.client.get("/addstudent")  

    @task
    def list_students(self):
        self.client.get("/list") 

    @task
    def add_student_post(self):
        self.client.post("/addrec", data={"name": "mostafa", "address": "123 Main St", "city": "Anytown", "pin": "12345"})
