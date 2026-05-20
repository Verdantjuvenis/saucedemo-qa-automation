import pytest
import requests

pytestmark = pytest.mark.api

@pytest.mark.api

def test_get_users_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    assert response.status_code == 200


def test_get_users_returns_list(users):
    assert isinstance(users, list)
    assert len(users) > 0


def test_first_user_has_required_fields(users):
    first_user = users[0]

    assert "id" in first_user
    assert "name" in first_user
    assert "email" in first_user

def test_user_data_values(users):
    for user in users:
        assert isinstance(user["id"], int)
        assert "@" in user["email"]
        assert len(user["name"]) > 0


def test_unique_user_ids(users):
    ids = [user["id"] for user in users]

    assert len(ids) == len(set(ids))

def test_specific_user(users):
    user = next(u for u in users if u["id"] == 1)

    assert user["name"] == "Leanne Graham"
    assert user["email"] == "Sincere@april.biz"

def test_create_user():
    payload = {
        "name": "Kev",
        "email": "kev@example.com"
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=payload
    )

    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "Kev"
    assert data["email"] == "kev@example.com"

def test_update_user():
    payload = {
        "name": "Kevin Updated",
        "email": "updated@example.com"
    }

    response = requests.put(
        "https://jsonplaceholder.typicode.com/users/1",
        json=payload
    )

    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Kevin Updated"
    assert data["email"] == "updated@example.com"

def test_delete_user():
    response = requests.delete("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200

def test_user_schema(users):
    for user in users:
        assert isinstance(user["id"], int)
        assert isinstance(user["name"], str)
        assert isinstance(user["username"], str)
        assert isinstance(user["email"], str)

        assert isinstance(user["address"], dict)
        assert isinstance(user["phone"], str)
        assert isinstance(user["website"], str)

        assert isinstance(user["company"], dict)

    def test_user_address_schema(users):
        for user in users:
            address = user["address"]

            assert isinstance(address["street"], str)
            assert isinstance(address["suite"], str)
            assert isinstance(address["city"], str)
            assert isinstance(address["zipcode"], str)

def test_get_invalid_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999"
    )

    assert response.status_code == 404

def test_get_invalid_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")

    assert response.status_code == 404
    assert response.json() == {}

def test_users_api_response_time():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )

    assert response.status_code == 200

def test_users_api_responds_under_two_seconds():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )

    assert response.elapsed.total_seconds() < 2