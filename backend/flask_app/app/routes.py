from flask import request, jsonify, render_template
from . import app
from .models import Questions, UserSubmissions
from . import database_helper, db


@app.route("/")
@app.route("/health")
def site_health():
    return "I'm running"


@app.route("/save", methods=["POST"])
def save_submission_details():
    submission_data = request.get_json()
    header_data = request.headers
    try:
        question_info = submission_data["question_info"]
        instance = database_helper.get_instance_or_add(Questions, **question_info)

        user_submission_info = submission_data["user_submission_info"]
        user_submission_info["user_id"] = header_data["user_id"]
        user_submission_info["question_id"] = instance.id
        database_helper.add_data(UserSubmissions, **user_submission_info)

        return jsonify({"status": "200"})
    except:
        return jsonify({"status": "400"})


@app.route("/get", methods=["GET"])
def get_submission_details():
    user_id = "def12334hh"
    data = (
        db.session.query(UserSubmissions, Questions)
        .join(Questions)
        .filter(UserSubmissions.user_id == user_id)
    )
    return render_template("home.html", title="Home", data=data, user_id=user_id)


@app.route("/login", methods=["GET"])
def login():

    return render_template("login.html", title="Login")
