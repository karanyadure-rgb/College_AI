from app.core.gemini import client


def ask_tutor(question, context=None):

    prompt = f"""
You are TSSM AI Tutor.

Help a diploma computer engineering student understand concepts
in a simple and clear way.

Context:
{context if context else "No additional context provided."}

Student Question:
{question}

Instructions:
- Give a clear and accurate answer.
- Use simple language.
- Explain step-by-step when necessary.
- Give an example when useful.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text