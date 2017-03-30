import unittest

from unittest.mock import patch

from usersservices.services.auth import auth
from usersservices.models.user import UserModel

class TestAuth(unittest.TestCase):

    def test_login_fail(self):
        self.assertFalse(auth('invalid user', 'invalid password'))

    @patch('usersservices.services.auth.find_user_by_email_and_password')
    def test_login_success(self, find_user):
        find_user.return_value = UserModel()
        self.assertTrue(auth('valid user', 'valid password'))

