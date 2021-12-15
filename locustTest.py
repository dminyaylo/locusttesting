from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    host = 'https://petstore.swagger.io/v2'


    @task(8)
    def add_user(self):
        self.client.post("/user", json={
            "id": 1,
            "username": "Dan",
            "firstName": "Dan",
            "lastName": "Min",
            "email": "Dan@gmail",
            "password": "loh123qweasdzxc",
            "phone": "666",
            "userStatus": 1
        })


    @task(3)
    def add_pet(self):
        self.client.post("/pet", json={
            "id": 1,
            "category": {
                "id": 1,
                "name": "sobaka"
            },
            "name": "Billy",
            "photoUrls": ["string"],
            "tags": [{
                "id": 1,
                "name": "dog"
            }],
            "status": "available"
        })


    @task(2)
    def update_pet(self):
        self.client.put("/pet", json={
            "id": 1,
            "category": {
                "id": 1,
                "name": "sobachka"
            },
            "name": "Billy2",
            "photoUrls": ["string"],
            "tags": [{
                "id": 1,
                "name": "pes"
            }],
            "status": "available"
        })


    @task(1)
    def create_user(self):
        self.client.get("/user/login", json={
            "username": "Dan",
            "password": "123qweasdzxc"
        })


    @task(7)
    def add_order(self):
        self.client.post("/store/order", json={
            "id": 1,
            "petId": 1,
            "quantity": 1,
            "shipDate": "2021-11-09T11:36:33.667Z",
            "status": "placed",
            "complete": True
        })


    @task(1)
    def get_order(self):
        self.client.get("/store/order/1")


    @task(1)
    def delete_order(self):
        self.client.delete("/store/order/1")


    @task(2)
    def update_user_ByName(self):
        self.client.put("/user/Dan", json={
            "id": 1,
            "username": "Dan",
            "firstName": "Loh",
            "lastName": "Min",
            "email": "dan@gmail",
            "password": "loh123qweasdzxc",
            "phone": "666",
            "userStatus": 1
        })


    @task(1)
    def get_user(self):
        self.client.get("/user/Dan")


    @task(1)
    def logout_user(self):
        self.client.get("/user/logout")