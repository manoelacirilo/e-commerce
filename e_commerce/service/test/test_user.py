import unittest

from e_commerce.model.user import User


class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        self.user = User.sign_up(name='Milo', email='milo@gmail.com', password='1234')

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
        with self.assertRaises(ValueError) as context:
            User.sign_up(name='', email='milo@gmail.com', password='1234')

        self.assertTrue('Registration not done' in str(context.exception))

    def test_login(self):
        # Given happens on setUp

        # When
        result = self.user.login(email='milo@gmail.com', password='1234')

        # Then
        self.assertEqual(result, 'Welcome Milo')
        self.assertTrue(self.user.logged)

    def test_login_fail(self):
        with self.assertRaises(ValueError) as context:
            self.user.login(email='milo@gamil', password='123')

        self.assertTrue('Invalid credentials' in str(context.exception))

    def test_check_password(self):
        self.assertTrue(self.user.check_password(password_to_check='1234'))

    def test_check_password_wrong(self):
        self.assertFalse(self.user.check_password(password_to_check='123'))

    def test_profile(self):
        # Given
        self.user.login(email='milo@gmail.com', password='1234')

        # When
        result = self.user.profile()

        # then
        self.assertEqual(result, f'Id: {self.user.id}\nName: Milo\nEmail: milo@gmail.com')

    def test_profile_fail(self):
        with self.assertRaises(ValueError) as context:
            self.user.profile()

        self.assertTrue('Unauthorized' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
