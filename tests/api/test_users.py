import pytest
from models.user import UsersListResponse, UserData, CreateUserResponse, UpdateUserResponse
from data.test_data import NEW_USER


@pytest.mark.api
@pytest.mark.smoke
class TestGetUsers:
    def test_get_users_returns_200(self, users_client):
        response = users_client.get_users()
        assert response.status_code == 200

    def test_get_users_response_schema(self, users_client):
        response = users_client.get_users(limit=5)
        body = UsersListResponse(**response.json())
        assert len(body.users) == 5
        assert body.total > 0

    def test_get_users_pagination(self, users_client):
        page1 = users_client.get_users(limit=5, skip=0).json()["users"]
        page2 = users_client.get_users(limit=5, skip=5).json()["users"]
        assert page1[0]["id"] != page2[0]["id"]

    def test_get_single_user_returns_200(self, users_client):
        response = users_client.get_user(user_id=1)
        assert response.status_code == 200

    def test_get_single_user_schema(self, users_client):
        response = users_client.get_user(user_id=1)
        body = UserData(**response.json())
        assert body.id == 1

    def test_get_nonexistent_user_returns_404(self, users_client):
        response = users_client.get_user(user_id=99999)
        assert response.status_code == 404

    def test_search_users_returns_results(self, users_client):
        response = users_client.search_users(query="Emily")
        assert response.status_code == 200
        body = UsersListResponse(**response.json())
        assert len(body.users) > 0


@pytest.mark.api
@pytest.mark.regression
class TestCreateUser:
    def test_create_user_returns_201(self, users_client):
        response = users_client.create_user(**NEW_USER)
        assert response.status_code == 201

    def test_create_user_response_has_id(self, users_client):
        response = users_client.create_user(**NEW_USER)
        body = CreateUserResponse(**response.json())
        assert body.id is not None
        assert body.firstName == NEW_USER["first_name"]
        assert body.lastName == NEW_USER["last_name"]


@pytest.mark.api
@pytest.mark.regression
class TestUpdateUser:
    def test_update_user_returns_200(self, users_client):
        response = users_client.update_user(user_id=1, firstName="Updated")
        assert response.status_code == 200

    def test_update_user_response_schema(self, users_client):
        response = users_client.update_user(user_id=1, firstName="Updated", lastName="Name")
        body = UpdateUserResponse(**response.json())
        assert body.firstName == "Updated"
        assert body.id == 1


@pytest.mark.api
@pytest.mark.regression
class TestDeleteUser:
    def test_delete_user_returns_200(self, users_client):
        response = users_client.delete_user(user_id=1)
        assert response.status_code == 200

    def test_delete_user_response_has_deleted_flag(self, users_client):
        response = users_client.delete_user(user_id=1)
        body = response.json()
        assert body.get("isDeleted") is True
