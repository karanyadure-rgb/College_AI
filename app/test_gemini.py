from app.core.gemini import client


response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain what a computer program is in one sentence."
)

print(response.text)