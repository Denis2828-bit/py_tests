import pytest
from models.user import LoginResponse
from data.test_data import VALID_USER, INVALID_USER


@pytest.mark.api
@pytest.mark.smoke
class TestLogin:
    def test_login_success(self, auth_client):
        response = auth_client.login(**VALID_USER)
        assert response.status_code == 200

    def test_login_returns_token(self, auth_client):
        response = auth_client.login(**VALID_USER)
        body = LoginResponse(**response.json())
        assert body.accessToken is not None
        assert len(body.accessToken) > 0

    def test_login_returns_user_data(self, auth_client):
        response = auth_client.login(**VALID_USER)
        body = LoginResponse(**response.json())
        assert body.username == VALID_USER["username"]
        assert body.firstName is not None

    def test_login_with_wrong_credentials_returns_400(self, auth_client):
        response = auth_client.login(**INVALID_USER)
        assert response.status_code == 400

    def test_login_error_has_message(self, auth_client):
        response = auth_client.login(**INVALID_USER)
        body = response.json()
        assert "message" in body

    def test_login_returns_refresh_token(self, auth_client):
        response = auth_client.login(**VALID_USER)
        body = response.json()               # превращаем ответ в словарь
        assert "refreshToken" in body        # проверяем что ключ есть


@pytest.mark.api
@pytest.mark.regression
class TestAuthMe:
    def test_get_me_with_valid_token(self, auth_client):
        token = auth_client.login(**VALID_USER).json()["accessToken"]
        response = auth_client.get_me(token)
        assert response.status_code == 200

    def test_get_me_returns_correct_user(self, auth_client):
        token = auth_client.login(**VALID_USER).json()["accessToken"]
        response = auth_client.get_me(token)
        body = response.json()
        assert body["username"] == VALID_USER["username"]

    def test_get_me_with_invalid_token_returns_error(self, auth_client):
        response = auth_client.get_me("invalid.token.here")
        # dummyjson returns 500 on malformed JWT (their API quirk)
        assert response.status_code in (401, 500)
