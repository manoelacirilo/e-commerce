from src.model.user import User


def main() -> None:
    client: User = User.sign_up(name='Kida', email='kida123@gmail.com', password='milo')
    # User.sign_up(name='Kida', email='kida123@gmail.com', password='')
    print(f'User {client} successfully registered.')

    client.login(email='kida123@gmail.com', password='milo')
    # client.login(email='123@gmail.com', password='mi')


if __name__ == '__main__':
    main()
