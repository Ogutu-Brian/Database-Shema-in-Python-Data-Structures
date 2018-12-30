from app.run import app
import pytest
app.config['TESTING'] = True
from app.api.v1.views import db

def client():
    client = app.test_client()
    return client


valid_user_data = {
    "headers": {
        "Content-Type": "application/json",
    },
    "data": {
        "sign-up": {
            "data": {
                "first_name": "Ogutu",
                "last_name": "Brian",
                "email": "codingbrian58@gmail.com",
                "password": "password"
            },
            "url": "/api/v1/users/sign-up"
        },
        "log-in": {
            "data": {
                "email": "codingbrian58@gmail.com",
                "password": "password"
            },
            "url": "/api/v1/users/log-in"
        }
    }
}
