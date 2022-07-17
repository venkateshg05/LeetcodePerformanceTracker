import requests


def get_access_token(GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET, request_token):
    url = f"https://github.com/login/oauth/access_token?client_id={GITHUB_CLIENT_ID}&client_secret={GITHUB_CLIENT_SECRET}&code={request_token}"
    headers = {"accept": "application/json"}
    res = requests.post(url, headers=headers)
    data = res.json()
    access_token = data["access_token"]

    return access_token


def get_user_data(access_token):
    access_token = "token " + access_token
    url = "https://api.github.com/user"
    headers = {"Authorization": access_token}

    resp = requests.get(url=url, headers=headers)

    userData = resp.json()

    return userData
