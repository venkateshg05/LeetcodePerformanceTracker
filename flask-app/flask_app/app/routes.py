from crypt import methods

from flask import request
from . import app
from .models import Users, db


@app.route("/")
@app.route("/health")
def site_health():
    return "I'm running"


@app.route("/save", methods=["POST"])
def save_data():
    problem_data = request.get_json()
    try:
        print(f"url: {problem_data['currURL']}, time: {problem_data['currTime']}s")
        return {"status": "200"}
    except:
        return {"status": "400"}


@app.route("/get", methods=["GET"])
def get_data():
    data = Users.query.all()
    try:
        print(data)
        return {"status": "200"}
    except:
        return {"status": "400"}
