from app.core.gemini import client


def explain_unit(unit, subject, topics:None):

    prompt = f"""
You are TSSM AI Tutor for Diploma Computer Engineering students.

Your task is to explain an academic unit using ONLY the
provided syllabus topics.

SUBJECT:
{subject}

UNIT:
{unit}

SYLLABUS TOPICS:
{topics}

Instructions:

1. Explain every topic from the provided syllabus.
2. Do not add unrelated topics.
3. Use simple student-friendly language.
4. Explain topics in the same order as the syllabus.
5. Start with a short unit overview.
6. Give a simple example wherever useful.
7. Highlight important exam points.
8. Explain difficult technical terms simply.
9. Use headings and bullet points.
10. Keep the explanation easy to revise.
11. Do not make up syllabus content.
12. Do not skip any provided topic.

--------------------------------------------------
RESPONSE FORMAT
--------------------------------------------------

# {unit}: {subject}

## 1. Unit Overview

Give a short and simple overview.

## 2. Detailed Explanation

Explain every syllabus topic in order.

For each topic use:

### Topic Name

**Definition:**

Give a simple definition.

**Explanation:**

Explain the concept clearly.

**Example:**

Give a simple practical example when useful.

**Key Points:**

- Important point
- Important point
- Important point

Continue until every provided syllabus topic
has been covered.

## 3. Important Exam Points

List the most important points to remember
for examinations.

## 4. Quick Revision

Give a short revision summary of the complete unit

Your final response should feel like a well-prepared study
guide created from the student's official syllabus.

Now generate the complete unit explanation.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text