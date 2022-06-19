import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Questions(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500))

    def __repr__(self) -> str:
        return f"{self.url}"
