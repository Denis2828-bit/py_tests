import requests
from requests import Response


class APIClient:
    """Base HTTP client. Wraps requests.Session with base_url and logging."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, path: str, headers: dict = None, **kwargs) -> Response:
        return self.session.get(f"{self.base_url}{path}", headers=headers, **kwargs)

    def post(self, path: str, **kwargs) -> Response:
        return self.session.post(f"{self.base_url}{path}", **kwargs)

    def put(self, path: str, **kwargs) -> Response:
        return self.session.put(f"{self.base_url}{path}", **kwargs)

    def patch(self, path: str, **kwargs) -> Response:
        return self.session.patch(f"{self.base_url}{path}", **kwargs)

    def delete(self, path: str, **kwargs) -> Response:
        return self.session.delete(f"{self.base_url}{path}", **kwargs)
