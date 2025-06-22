from locust import HttpUser, task, between

class PetStoreUser(HttpUser):
    host = "https://petstore.swagger.io/v2"
    wait_time = between(1, 3)

    @task(2)
    def get_pets_by_status(self):
        self.client.get("/pet/findByStatus?status=available")

    @task(1)
    def get_pet_by_id(self):
        self.client.get("/pet/1")

    @task(1)
    def place_order(self):
        self.client.post(
            "/store/order",
            json={
                "id": 1234,
                "petId": 1,
                "quantity": 1,
                "shipDate": "2025-06-13T16:00:00Z",
                "status": "placed",
                "complete": True
            }
        )

    @task(1)
    def get_inventory(self):
        self.client.get("/store/inventory")
