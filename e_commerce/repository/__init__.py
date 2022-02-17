from e_commerce.model import db
from e_commerce.repository.user_repository import UserRepository

user_repository = UserRepository(db)
