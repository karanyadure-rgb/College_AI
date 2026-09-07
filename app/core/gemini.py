from google import genai

from app.core.config import GEMINI_API_KEY


if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not configured")


client = genai.Client(
    api_key=GEMINI_API_KEY
)