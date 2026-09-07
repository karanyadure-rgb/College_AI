from flask import Flask

from app.tutor.router import tutor_router


app = Flask(__name__)

app.register_blueprint(tutor_router)


@app.route("/")
def home():
    return {
        "message": "TSSM AI Backend is running"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )