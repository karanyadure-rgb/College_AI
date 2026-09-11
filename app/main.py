from flask import Flask

from app.tutor.router import tutor_router
from app.unit_explanation.router import unit_explanation_router
from app.exam_answer.router import exam_answer_router
from app.summarization.router import summarization_router


app = Flask(__name__)

app.register_blueprint(tutor_router)
app.register_blueprint(unit_explanation_router)
app.register_blueprint(exam_answer_router)
app.register_blueprint(summarization_router)


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