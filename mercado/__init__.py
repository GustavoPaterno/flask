from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager()
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = '5021d990913aae5d508cb9ce'
db.init_app(app)
Bcrypt = Bcrypt(app)

from mercado import routes
