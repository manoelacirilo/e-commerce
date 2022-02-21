from flask import Flask
from flask_restful import Api

from e_commerce.controller.products_controller import blueprint as products_controller_blueprint
from e_commerce.controller.users_controller import blueprint as users_controller_blueprint

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config.from_object('config')
app.register_blueprint(users_controller_blueprint)
app.register_blueprint(products_controller_blueprint)

api = Api(app)
