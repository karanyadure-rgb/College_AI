from flask import Blueprint, request, jsonify
from app.exam_answer.service import generate_exam_answer

exam_answer_router = Blueprint(
    "exam_answer",
    __name__
)

@exam_answer_router.route(
    "/api/exam-answer",
    methods=["POST"]
)
def exam_answer():

    data = request.get_json()

    question = data.get("question")
    marks = data.get("marks")
    context = data.get("context")

    if not question:
        return jsonify({
            "error":"Question is required"
        }), 400

    if not marks:
        return jsonify({
            "error": "Marks are required"
        }), 400

    answer = generate_exam_answer(
        question=question,
        marks=marks,
        context=context
    )

    return jsonify({
        "answer": answer
    })