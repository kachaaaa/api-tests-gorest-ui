import requests
from config.config import BASE_URL, TOKEN

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def get_users():
    return requests.get(f"{BASE_URL}/users", headers=HEADERS)

def get_user_by_id(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}", headers=HEADERS)

def create_user(data):
    return requests.post(f"{BASE_URL}/users", headers=HEADERS, json=data)


def delete_user(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    return requests.delete(url, headers=headers)