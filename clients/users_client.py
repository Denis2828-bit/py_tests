from clients.api_client import APIClient
from requests import Response


class UsersClient:
    """All requests related to /users endpoint."""

    def __init__(self, client: APIClient):
        self.client = client

    def get_users(self, limit: int = 10, skip: int = 0) -> Response:
        return self.client.get("/users", params={"limit": limit, "skip": skip})

    def get_user(self, user_id: int) -> Response:
        return self.client.get(f"/users/{user_id}")

    def search_users(self, query: str) -> Response:
        return self.client.get("/users/search", params={"q": query})

    def create_user(self, first_name: str, last_name: str, age: int) -> Response:
        return self.client.post("/users/add", json={
            "firstName": first_name,
            "lastName": last_name,
            "age": age,
        })

    def update_user(self, user_id: int, **fields) -> Response:
        return self.client.patch(f"/users/{user_id}", json=fields)

    def delete_user(self, user_id: int) -> Response:
        return self.client.delete(f"/users/{user_id}")


class AuthClient:
    """Requests related to /auth endpoint."""

    def __init__(self, client: APIClient):
        self.client = client

    def login(self, username: str, password: str) -> Response:
        return self.client.post("/auth/login", json={
            "username": username,
            "password": password,
        })

    def get_me(self, token: str) -> Response:
        return self.client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
