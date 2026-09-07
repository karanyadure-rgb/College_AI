from flask import Blueprint, request, jsonify

from app.tutor.service import ask_tutor


tutor_router = Blueprint("tutor", __name__)


@tutor_router.route("/api/tutor", methods=["POST"])
def tutor():

    data = request.get_json()

    question = data.get("question")
    context = data.get("context")

    if not question:
        return jsonify({
            "error": "Question is required"
        }), 400

    answer = ask_tutor(
        question=question,
        context=context
    )

    return jsonify({
        "answer": answer
    })