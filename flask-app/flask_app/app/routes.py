from crypt import methods

from flask import request
from . import app


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
