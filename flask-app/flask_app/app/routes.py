from crypt import methods

from flask import request
from . import app
from .models import Questions, db


@app.route("/")
@app.route("/health")
def site_health():
    return "I'm running"


@app.route("/save", methods=["POST"])
def save_data():
    problem_data = request.get_json()
    try:
        print(f"url: {problem_data['currURL']}, time: {problem_data['currTime']}s")
        url = problem_data["currURL"]
        question = Questions(url=url)
        db.session.add(question)
        db.session.commit()
        return {"status": "200"}
    except:
        return {"status": "400"}


@app.route("/get", methods=["GET"])
def get_data():
    data = Questions.query.all()
    try:
        print(data)
        return {"status": "200"}
    except:
        return {"status": "400"}
