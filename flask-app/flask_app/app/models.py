import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Questions(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    difficulty_tag = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"{self.id}- {self.url}"


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(500), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    submission_dt = db.Column(db.DateTime(timezone=True), nullable=False)
    submission_status = db.Column(db.Enum(["Accepted", "Failed"]))

    def __repr__(self) -> str:
        return f"{self.user_id}, {self.question_id}, {self.submission_dt}"
