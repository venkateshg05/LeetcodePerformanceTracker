from crypt import methods

from flask import request
from . import app
from .models import Questions, db
from . import database_helper


@app.route("/")
@app.route("/health")
def site_health():
    return "I'm running"


@app.route("/save", methods=["POST"])
def save_data():
    problem_data = request.get_json()
    try:
        url = problem_data["currURL"]
        data = {"url": url}
        database_helper.add_data(Questions, **data)
        return {"status": "200"}
    except:
        return {"status": "400"}


@app.route("/get", methods=["GET"])
def get_data():
    data = database_helper.get_all_data(Questions)
    try:
        data = [row.url for row in data]
        return {"data": data, "status": "200"}
    except:
        return {"status": "400"}
