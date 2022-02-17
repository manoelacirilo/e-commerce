from flask import Flask
from flask_restful import Api

from e_commerce.controller.users_controller import UsersController

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

api = Api(app)

api.add_resource(UsersController, '/users')
# api.add_resource(UserController, '/users/<int:id>')
# api.add_resource(ProductsController, '/products')
# api.add_resource(ProductController, '/products/<int:id>')
