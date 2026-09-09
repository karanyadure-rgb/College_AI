import streamlit as st
import requests


st.set_page_config(
    page_title="TSSM LearnSync",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# HOME
# -----------------------------

st.title("TSSM LearnSync")
st.write("Your AI Study Companion")

st.markdown("## Hello, Karan 👋")
st.write("What do you want to do today?")


# -----------------------------
# AI TUTOR
# -----------------------------

st.markdown("### 🤖 AI Tutor")
st.write("Ask any question about your studies.")

if st.button("Ask a Question", use_container_width=True):

    st.session_state["mode"] = "tutor"


# -----------------------------
# TUTOR SCREEN
# -----------------------------

if st.session_state.get("mode") == "tutor":

    st.divider()

    st.subheader("🤖 AI Tutor")

    question = st.text_area(
        "Ask your question",
        placeholder="Example: What is an operating system?"
    )

    context = st.text_area(
        "Context (optional)",
        placeholder="Example: Operating System Unit 1"
    )

    if st.button("Get Answer", use_container_width=True):

        if not question.strip():

            st.warning("Please enter a question.")

        else:

            try:

                response = requests.post(
                    "http://127.0.0.1:5000/api/tutor",
                    json={
                        "question": question,
                        "context": context
                    }
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success("Answer")

                    st.write(data["answer"])

                else:

                    st.error(
                        f"Backend error: {response.status_code}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to Flask. "
                    "Make sure your Flask server is running."
                )


# -----------------------------
# SUMMARIZE AI
# -----------------------------

st.divider()

st.markdown("### 📝 Summarize")

if st.button(
    "Make your notes shorter",
    use_container_width=True
):
    st.info("Summarization will be added next.")

# -----------------------------
# EXPLAIN AI
# -----------------------------

st.markdown("### 📚 Explain Unit")

if st.button(
    "Understand a unit easily",
    use_container_width=True
):
    st.session_state["mode"] = "unit_explanation"

if st.session_state.get("mode") == "unit_explanation":

    st.divider()

    st.subheader("📚 Unit Explanation")

    subject = st.text_input(
        "Subject",
        placeholder="Example: Software Engineering"
    )

    unit = st.text_input(
        "Unit",
        placeholder="Example: Unit II - Software Requirement Engineering"
    )

    topics = st.text_area(
        "Syllabus Topics",
        placeholder="Enter the official syllabus topics here..."
    )

    if st.button("Explain Unit", use_container_width=True):

        if not subject.strip():
            st.warning("Please enter the subject.")

        elif not unit.strip():
            st.warning("Please enter the unit.")

        elif not topics.strip():
            st.warning("Please enter the syllabus topics.")

        else:

            try:

                topic_list = [
                    topic.strip()
                    for topic in topics.split("\n")
                    if topic.strip()
                ]

                response = requests.post(
                    "http://127.0.0.1:5000/api/unit-explanation",
                    json={
                        "subject": subject,
                        "unit": unit,
                        "topics": topic_list
                    }
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success("Unit Explanation")

                    st.markdown(
                        data["explanation"]
                    )

                else:

                    st.error(
                        f"Backend error: {response.status_code}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to Flask. "
                    "Make sure your Flask server is running."
                )


st.markdown("### ✍️ Exam Answer")

if st.button(
    "Generate exam-ready answer",
    use_container_width=True
):
    st.info("Exam Answer Generation will be added next.")