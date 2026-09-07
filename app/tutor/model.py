from dataclasses import dataclass
from typing import Optional


@dataclass
class TutorRequest:
    question: str
    context: Optional[str] = None


@dataclass
class TutorResponse:
    answer: str