from e_commerce.model import db
from e_commerce.repository.cart_repository import CartRepository
from e_commerce.repository.item_repository import ItemRepository
from e_commerce.repository.product_repository import ProductRepository
from e_commerce.repository.user_repository import UserRepository

user_repository = UserRepository(db)
product_repository = ProductRepository(db)
cart_repository = CartRepository(db)
item_repository = ItemRepository(db)
