import streamlit as st
import requests


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="TSSM LearnSync",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .ky-logo {
        width: 55px;
        height: 55px;
        border-radius: 50%;
        background: linear-gradient(135deg, #123B78, #2563EB);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .logo-title {
        font-size: 22px;
        font-weight: 700;
        color: #123B78;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="ky-logo">KY</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="logo-title">TSSM LearnSync</div>',
        unsafe_allow_html=True
    )

    st.markdown("### AI Features")

    if st.button(
        "🤖 AI Tutor",
        use_container_width=True
    ):
        st.session_state["mode"] = "tutor"

    if st.button(
        "📚 Unit Explanation",
        use_container_width=True
    ):
        st.session_state["mode"] = "unit_explanation"

    if st.button(
        "✍️ Exam Answer",
        use_container_width=True
    ):
        st.session_state["mode"] = "exam_answer"

    if st.button(
        "📝 Summarizer",
        use_container_width=True
    ):
        st.session_state["mode"] = "summarizer"


# --------------------------------------------------
# DEFAULT MODE
# --------------------------------------------------

if "mode" not in st.session_state:
    st.session_state["mode"] = "tutor"


# ==================================================
# AI TUTOR
# ==================================================

if st.session_state["mode"] == "tutor":

    st.title("🤖 AI Tutor")

    st.write(
        "Ask questions and get clear explanations "
        "from your AI study assistant."
    )

    st.divider()

    question = st.text_area(
        "Your Question",
        placeholder="Example: What is an operating system?"
    )

    context = st.text_area(
        "Context (optional)",
        placeholder="Example: Operating System Unit 1"
    )

    if st.button(
        "Get Answer",
        use_container_width=True
    ):

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

                    st.markdown(data["answer"])

                else:

                    st.error(
                        f"Backend error: {response.status_code}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to Flask. "
                    "Make sure your Flask server is running."
                )


# ==================================================
# UNIT EXPLANATION
# ==================================================

elif st.session_state["mode"] == "unit_explanation":

    st.title("📚 Unit Explanation")

    st.write(
        "Understand your complete syllabus unit "
        "in simple and exam-oriented language."
    )

    st.divider()

    subject = st.text_input(
        "Subject",
        placeholder="Example: Software Engineering"
    )

    unit = st.text_input(
        "Unit",
        placeholder="Example: Unit II - Software Requirement Engineering"
    )

    topics = st.text_area(
        "Official Syllabus Topics",
        placeholder=(
            "Enter each syllabus topic on a new line.\n\n"
            "Example:\n"
            "2.1 Software Engineering Core Principles\n"
            "2.2 Software Practices\n"
            "2.3 Requirement Engineering\n"
            "2.4 Software Requirement Specification"
        ),
        height=180
    )

    if st.button(
        "Explain Unit",
        use_container_width=True
    ):

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


# ==================================================
# EXAM ANSWER
# ==================================================

elif st.session_state["mode"] == "exam_answer":

    st.title("✍️ Exam Answer Generator")

    st.write(
        "Generate exam-ready answers according "
        "to the marks."
    )

    st.divider()

    question = st.text_area(
        "Enter your question",
        placeholder=(
            "Example: What is Software Requirement Specification?"
        )
    )

    marks = st.selectbox(
        "Select Marks",
        [2, 4, 6]
    )

    context = st.text_input(
        "Context (optional)",
        placeholder="Example: Software Engineering Unit II"
    )

    if st.button(
        "Generate Answer",
        use_container_width=True
    ):

        if not question.strip():

            st.warning("Please enter a question.")

        else:

            try:

                response = requests.post(
                    "http://127.0.0.1:5000/api/exam-answer",
                    json={
                        "question": question,
                        "marks": marks,
                        "context": context
                    }
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success("Exam-ready Answer")

                    st.markdown(
                        data["answer"]
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


# ==================================================
# SUMMARIZER
# ==================================================

elif st.session_state["mode"] == "summarizer":

    st.title("📝 Summarizer")

    st.write(
        "Summarize your study material into "
        "clear and easy-to-revise notes."
    )

    st.divider()

    # Text input area
    text = st.text_area(
        "Study Material",
        placeholder=(
            "Paste your study material here..."
        ),
        height=220
    )

    # Add file button
    col1, col2 = st.columns([8, 1])

    with col2:
        add_file = st.button(
            "+",
            help="Upload PDF or DOCX"
        )

    uploaded_file = None

    if add_file:

        uploaded_file = st.file_uploader(
            "Upload study material",
            type=["pdf", "docx"],
            label_visibility="collapsed"
        )

    summary_length = st.selectbox(
        "Summary Length",
        ["short", "medium", "detailed"],
        index=1
    )

    if st.button(
        "Generate Summary",
        use_container_width=True
    ):

        if not text.strip() and uploaded_file is None:

            st.warning(
                "Please paste text or upload a PDF/DOCX file."
            )

        else:

            try:

                files = None
                data = {
                    "summary_length": summary_length
                }

                if uploaded_file:

                    files = {
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            uploaded_file.type
                        )
                    }

                else:

                    data["text"] = text

                response = requests.post(
                    "http://127.0.0.1:5000/api/summarize",
                    data=data,
                    files=files
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Summary")

                    st.markdown(
                        result["summary"]
                    )

                else:

                    error = response.json()

                    st.error(
                        error.get(
                            "error",
                            "Something went wrong."
                        )
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to Flask. "
                    "Make sure your Flask server is running."
                )