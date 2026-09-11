from flask import Blueprint, request, jsonify
from app.summarization.service import summarize_text
from app.summarization.extractor import extract_text


summarization_router = Blueprint(
    "summarization",
    __name__
)


@summarization_router.route(
    "/api/summarize",
    methods=["POST"]
)
def summarize():

    text = request.form.get("text")
    summary_length = request.form.get(
        "summary_length",
        "medium"
    )

    uploaded_file = request.files.get("file")

    # If a file is uploaded
    if uploaded_file:

        try:

            text = extract_text(
                uploaded_file,
                uploaded_file.filename
            )

        except ValueError as error:

            return jsonify({
                "error": str(error)
            }), 400

    # Check if text is available
    if not text or not text.strip():

        return jsonify({
            "error": "Please provide text or upload a PDF/DOCX file."
        }), 400

    summary = summarize_text(
        text=text,
        summary_length=summary_length
    )

    return jsonify({
        "summary": summary
    })