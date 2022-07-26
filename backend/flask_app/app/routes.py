from flask import redirect, request, jsonify, render_template, url_for, session
from . import app
from .models import Questions, UserSubmissions
from . import database_helper, db
from . import config
from .helpers import get_access_token, get_user_data


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


@app.route("/home", methods=["GET"])
def get_submission_details():
    ## TODO Move to decorator, use header (like in /save)
    ## TODO save token to browser local
    access_token = session.get("access_token")
    if access_token is None:
        return redirect(url_for("login"))

    user_data = get_user_data(access_token)
    user_id = user_data["login"]
    user_email = user_data["email"]
    data = (
        db.session.query(UserSubmissions, Questions)
        .join(Questions)
        .filter(UserSubmissions.user_id == "def12334hh")
    )
    return render_template(
        "home.html", title="Home", data=data, user_id=user_id, user_email=user_email
    )


@app.route("/github_redirect", methods=["GET"])
def redirect_after_auth():
    args = request.args
    request_token = args.get("code")
    access_token = get_access_token(
        config.GITHUB_CLIENT_ID, config.GITHUB_CLIENT_SECRET, request_token
    )
    session["access_token"] = access_token
    redirect_obj = redirect(url_for("get_submission_details"))
    return redirect_obj


@app.route("/login", methods=["GET"])
def login():

    return render_template(
        "login.html", github_client_id=config.GITHUB_CLIENT_ID, title="Login"
    )
