from utils.api_client import create_user, delete_user


def test_delete_user_success():
    user_data = {
        "name": "Delete Test User",
        "gender": "male",
        "email": "delete_user_123@example.com",
        "status": "active"
    }

    create_response = create_user(user_data)
    assert create_response.status_code == 201

    user_id = create_response.json()["id"]

    delete_response = delete_user(user_id)
    assert delete_response.status_code == 204


def test_delete_user_not_found():
    delete_response = delete_user(999999999)
    assert delete_response.status_code == 404