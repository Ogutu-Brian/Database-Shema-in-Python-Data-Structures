import pytest
import unittest
from .import client, valid_user_data, db
import json


class TestUser(unittest.TestCase):
    """Tests user operations performed on a user"""

    def test_unexisting_account(self):
        headers = valid_user_data.get("headers")
        data = valid_user_data["data"].get("log-in")["data"]
        url = valid_user_data["data"].get("log-in")["url"]
        result = self.login(url=url, data=data, headers=headers)
        self.assertEqual("error", result["status"])
        db.tear_down()

    def test_valid_sign_up(self):
        """tests if a user without an account can sign up"""
        headers = valid_user_data.get("headers")
        data = valid_user_data["data"].get("sign-up")["data"]
        url = valid_user_data["data"].get("sign-up")["url"]
        result = self.sign_up(url=url, data=data, headers=headers)
        self.assertEqual("success", result["status"])
        db.tear_down()

    def test_existing_account(self):
        """Tests for an attempt to sign up with an existing account"""
        headers = valid_user_data.get("headers")
        data = valid_user_data["data"].get("sign-up")["data"]
        url = valid_user_data["data"].get("sign-up")["url"]
        self.sign_up(url=url, data=data, headers=headers)
        result = self.sign_up(url=url, data=data, headers=headers)
        self.assertEqual("error", result["status"])
        db.tear_down()

    def test_valid_log_in(self):
        """Tests if a user with an account can log in"""
        headers = valid_user_data.get("headers")
        data = valid_user_data["data"].get("sign-up")["data"]
        url = valid_user_data["data"].get("sign-up")["url"]
        self.sign_up(url=url, data=data, headers=headers)

        headers = valid_user_data.get("headers")
        data = valid_user_data["data"].get("log-in")["data"]
        url = valid_user_data["data"].get("log-in")["url"]
        result = self.login(url=url, data=data, headers=headers)
        self.assertEqual("success", result["status"])
        db.tear_down()

    def login(self, url="", data={}, headers={}):
        "A method for logging into the system"
        result = client().post(url, data=json.dumps(data), headers=headers)
        return json.loads(result.get_data(as_text=True))

    def sign_up(self, url="", data={}, headers={}):
        """sign up method for the test client"""
        result = client().post(url, data=json.dumps(data), headers=headers)
        return json.loads(result.get_data(as_text=True))
