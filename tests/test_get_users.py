from utils.api_client import get_users, get_user_by_id

def test_get_users_success():
    response = get_users()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_not_found():
    response = get_user_by_id(999999)
    assert response.status_code == 404