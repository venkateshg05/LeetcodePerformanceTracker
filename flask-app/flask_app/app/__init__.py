from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import config

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

from . import routes, models
