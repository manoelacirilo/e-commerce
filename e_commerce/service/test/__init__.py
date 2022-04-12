from flask import Flask

from e_commerce.model import db


def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://manoelacirilo:1907@localhost/e_commerce_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.app_context().push()
    return app
