import pytest
import unittest
from .import client
import json


class TestUser(unittest.TestCase):
    """Tests user operations performed on a user"""

    def test_unexisting_account(self):
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "email": "codingbrian58@gmail.com",
            "password": "password"
        }
        url = '/api/v1/users/log-in'
        result = self.login(url=url, data=data, headers=headers)
        self.assertEqual("error", result["status"])

    def login(self, url="", data={}, headers={}):
        "A method for logging into the system"
        result = client().post(url, data=json.dumps(data), headers=headers)
        return json.loads(result.get_data(as_text=True))

    def sign_up(self, url="", data={}, headers={}):
        """sign up method for the test client"""
        result = client().post(url, data=json.dumps(data), headers=headers)
        return json.loads(result.get_data(as_text=True))
