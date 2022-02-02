import unittest

from src.model.user import User


class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        self.user = User.sign_up(name='Milo', email='milo@gamail.com', password='1234')

    def test_signup(self):
        # Given
        name = 'Milo'
        email = 'milo@gmail.com'
        password = '1234'

        # When
        user = User.sign_up(name, email, password)

        # Then
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        self.assertFalse(user.logged)

    def test_signup_fail(self):
        with self.assertRaises(ValueError):
            User.sign_up(name='', email='milo@gamil.com', password='1234')

    def test_login(self):
        result = self.user.login(email='milo@gamail.com', password='1234')

        self.assertEqual(result, 'Welcome Milo')
        self.assertTrue(self.user.logged)

    def test_login_fail(self):
        with self.assertRaises(ValueError):
            self.user.login(email='milo@gamil', password='123')

    def test_check_password(self):
        self.assertTrue(self.user.check_password(password_to_check='1234'))

    def test_check_password_wrong(self):
        self.assertFalse(self.user.check_password(password_to_check='123'))


if __name__ == '__main__':
    unittest.main()
