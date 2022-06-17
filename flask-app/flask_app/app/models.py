import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
