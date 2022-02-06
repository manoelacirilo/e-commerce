from src.model.product import Product
from src.model.user import User


def main() -> None:
    client: User = User.sign_up(name='Kida', email='kida123@gmail.com', password='milo')
    # User.sign_up(name='Kida', email='kida123@gmail.com', password='')
    print(f'User {client} successfully registered.')

    client.login(email='kida123@gmail.com', password='milo')
    # client.login(email='123@gmail.com', password='mi')
    products = populate_products()
    for product in products:
        print(f'Product: {product.name} registered. Price: {product.price}')


def populate_products() -> list[Product]:
    return [Product.register(name=f'Product-{index}', price=10 * (index + 1)) for index in range(10)]


if __name__ == '__main__':
    main()
