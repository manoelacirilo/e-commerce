import unittest

from src.model.user import User


class TestUser(unittest.TestCase):

    def test_signup(self):
        # Given
        name = 'Milo'
        email = 'milo@gmail.com'
        password = '1234'

        # When
        user = User.sign_up(name, email, password)

        # Then
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        self.assertFalse(user.logged)

    def test_signup_fail(self):
        with self.assertRaises(ValueError):
            User.sign_up(name='', email='milo@gamil.com', password='1234')


if __name__ == '__main__':
    unittest.main()
