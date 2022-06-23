from . import db
from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime


class utcnow(expression.FunctionElement):
    type = DateTime()


@compiles(utcnow, "postgresql")
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


class Questions(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False, unique=True)
    difficulty_tag = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"id: {self.id}; url: {self.url}"


class UserSubmissions(db.Model):
    __tablename__ = "user_submissions"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(500), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    submission_dt = db.Column(
        db.DateTime(timezone=True), server_default=utcnow(), nullable=False
    )
    # submission_dt = db.Column(db.String(500), nullable=False)
    submission_status = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"{self.user_id}, {self.question_id}, {self.submission_dt}"
