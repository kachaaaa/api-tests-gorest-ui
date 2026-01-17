from utils.api_client import create_user
import uuid

def test_create_user_success():
    unique_email = f"user_{uuid.uuid4()}@example.com"

    data = {
        "name": "ui Test User",
        "email": unique_email,
        "gender": "male",
        "status": "active"
    }

    response = create_user(data)
    assert response.status_code == 201

def test_create_user_no_name():
    data = {
        "email": "noname@example.com",
        "gender": "female",
        "status": "active"
    }

    response = create_user(data)
    assert response.status_code == 422

    def test_create_user_empty_body():
        response = create_user({})

        assert response.status_code == 422