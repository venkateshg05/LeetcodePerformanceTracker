from . import app


@app.route("/")
@app.route("/health")
def site_health():
    return "I'm running"
