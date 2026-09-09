from flask import Blueprint, request, jsonify
from app.unit_explanation.service import explain_unit


unit_explanation_router = Blueprint(
    "unit_explanation",
    __name__
)


@unit_explanation_router.route(
    "/api/unit-explanation",
    methods=["POST"]
)
def unit_explanation():

    data = request.get_json()

    unit = data.get("unit")
    subject = data.get("subject")
    topics = data.get("topics")

    if not unit:
        return jsonify({
            "error": "Unit is required"
        }), 400

    if not subject:
        return jsonify({
            "error": "Subject is required"
        }), 400

    if not topics:
        return jsonify({
            "error": "Topics are required"
        }), 400

    explanation = explain_unit(
        unit=unit,
        subject=subject,
        topics=topics
    )

    return jsonify({
        "explanation": explanation
    })