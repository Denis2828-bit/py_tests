import os
import pytest
from dotenv import load_dotenv
from clients.api_client import APIClient
from clients.users_client import UsersClient, AuthClient

load_dotenv()


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://reqres.in")


@pytest.fixture(scope="session")
def api_client(base_url) -> APIClient:
    return APIClient(base_url)


@pytest.fixture(scope="session")
def users_client(api_client) -> UsersClient:
    return UsersClient(api_client)


@pytest.fixture(scope="session")
def auth_client(api_client) -> AuthClient:
    return AuthClient(api_client)


# Playwright fixtures are provided automatically by pytest-playwright.
# Base UI URL fixture for UI tests.
@pytest.fixture(scope="session")
def base_ui_url() -> str:
    return os.getenv("BASE_UI_URL", "https://reqres.in")
