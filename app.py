import streamlit as st
from prompt_template import build_prompt
from llm import generate_response

st.set_page_config(
    page_title="Aura Prompt Engineering",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(124, 58, 237, 0.18), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(6, 182, 212, 0.18), transparent 25%),
        radial-gradient(circle at 50% 100%, rgba(236, 72, 153, 0.12), transparent 30%),
        #080d1a;
    color: #ffffff;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

.hero {
    padding: 35px;
    border-radius: 24px;
    background: linear-gradient(
        135deg,
        #312e81,
        #155e75,
        #831843
    );
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 20px 50px rgba(0,0,0,0.35);
    margin-bottom: 25px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    color: #ffffff !important;
}

.hero-subtitle {
    font-size: 17px;
    color: #f1f5f9 !important;
    margin-top: 10px;
}

.card {
    background: #111827;
    border: 1px solid #334155;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

.card-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 15px;
    color: #ffffff !important;
}

p {
    color: #e2e8f0 !important;
}

.stMarkdown {
    color: #e2e8f0;
}

label {
    color: #f8fafc !important;
    font-weight: 600 !important;
}

div[data-baseweb="select"] > div {
    background-color: #1e293b !important;
    border: 1px solid #64748b !important;
    border-radius: 12px !important;
}

div[data-baseweb="select"] span {
    color: #ffffff !important;
}

div[data-baseweb="select"] input {
    color: #ffffff !important;
}

div[role="listbox"] {
    background-color: #1e293b !important;
}

div[role="option"] {
    color: #ffffff !important;
    background-color: #1e293b !important;
}

div[role="option"]:hover {
    background-color: #4c1d95 !important;
    color: #ffffff !important;
}

textarea {
    background-color: #f8fafc !important;
    color: #0f172a !important;
    border: 2px solid #6366f1 !important;
    border-radius: 12px !important;
    font-size: 15px !important;
}

textarea::placeholder {
    color: #64748b !important;
    opacity: 1 !important;
}

div[data-testid="stSlider"] label {
    color: #f8fafc !important;
}

div[data-testid="stSlider"] [data-testid="stMarkdownContainer"] {
    color: #e2e8f0 !important;
}

.stButton > button {
    width: 100%;
    height: 52px;
    border: none !important;
    border-radius: 14px;
    font-size: 17px;
    font-weight: 700;
    color: #ffffff !important;
    background: linear-gradient(
        90deg,
        #7c3aed,
        #0891b2,
        #db2777
    );
    box-shadow: 0 10px 25px rgba(124, 58, 237, 0.4);
}

.stButton > button:hover {
    color: #ffffff !important;
    background: linear-gradient(
        90deg,
        #6d28d9,
        #0e7490,
        #be185d
    );
}

.badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 999px;
    background: #312e81;
    border: 1px solid #818cf8;
    color: #ffffff !important;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 15px;
}

.answer-box {
    padding: 25px;
    border-radius: 18px;
    background: #0f172a;
    border: 1px solid #22d3ee;
    line-height: 1.8;
    color: #f8fafc !important;
    font-size: 16px;
}

.answer-box p,
.answer-box span,
.answer-box div {
    color: #f8fafc !important;
}

div[data-testid="stMetric"] {
    background: #1e293b;
    border: 1px solid #475569;
    padding: 15px;
    border-radius: 14px;
}

div[data-testid="stMetricLabel"] {
    color: #cbd5e1 !important;
}

div[data-testid="stMetricValue"] {
    color: #ffffff !important;
}

details {
    background: #111827 !important;
    border: 1px solid #475569 !important;
    border-radius: 14px !important;
}

details summary {
    color: #ffffff !important;
    font-weight: 600 !important;
}

details p {
    color: #e2e8f0 !important;
}

pre {
    background-color: #020617 !important;
    color: #e2e8f0 !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
}

section[data-testid="stSidebar"] {
    background: #0f172a !important;
    border-right: 1px solid #334155;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label {
    color: #e2e8f0 !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
}

div[data-testid="stAlert"] {
    color: #ffffff !important;
}

.footer {
    text-align: center;
    color: #94a3b8 !important;
    padding: 30px 0 10px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

techniques = [
    "Zero-shot",
    "One-shot",
    "Few-shot",
    "CoT",
    "Manual CoT",
    "ToT",
    "React",
    "Direct Stimulus Prompting",
    "Self-consistency",
    "Role based",
    "Instruction tuning"
]

technique_info = {
    "Zero-shot": "No examples",
    "One-shot": "One example",
    "Few-shot": "Multiple examples",
    "CoT": "Chain of Thought",
    "Manual CoT": "Explicit reasoning",
    "ToT": "Tree of Thoughts",
    "React": "Reason + Act",
    "Direct Stimulus Prompting": "Direct cues",
    "Self-consistency": "Multiple reasoning paths",
    "Role based": "Expert role prompting",
    "Instruction tuning": "Instruction-focused prompting"
}

descriptions = {
    "Zero-shot": "Ask the model to perform a task without providing examples.",
    "One-shot": "Provide one example to guide the expected output.",
    "Few-shot": "Provide multiple examples to help the model understand the pattern.",
    "CoT": "Encourages structured step-by-step reasoning.",
    "Manual CoT": "Provides an explicit reasoning structure for the model.",
    "ToT": "Explores multiple possible reasoning paths before selecting an answer.",
    "React": "Combines reasoning with actions or external tools.",
    "Direct Stimulus Prompting": "Uses direct cues to guide the model toward the desired response.",
    "Self-consistency": "Uses multiple reasoning paths and selects the most consistent answer.",
    "Role based": "Assigns the model a specific role or expert identity.",
    "Instruction tuning": "Uses clear instructions to guide the model toward a specific task."
}

with st.sidebar:
    st.markdown("## 🤖 Aura AI")

    st.markdown(
        """
        <div style="
            padding:15px;
            border-radius:15px;
            background:linear-gradient(
                135deg,
                rgba(124,58,237,.25),
                rgba(6,182,212,.15)
            );
            border:1px solid rgba(255,255,255,.1);
        ">
            <b style="color:white;">Prompt Engineering Lab</b><br>
            <span style="color:#cbd5e1;">
            Explore powerful prompting techniques for LLMs.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown("### ✨ Prompting Techniques")

    for name in techniques:
        st.markdown(
            f"""
            <div style="
                padding:8px 0;
                color:#ffffff;
                font-size:13px;
            ">
                <b>{name}</b><br>
                <span style="color:#94a3b8;">
                {technique_info[name]}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.caption("🚀 Powered by Hugging Face LLM")

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">
            🤖 Aura Prompt Engineering
        </div>
        <div class="hero-subtitle">
            Experiment with different prompt engineering techniques
            and compare their effectiveness using a Hugging Face LLM.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">🎯 Prompt Configuration</div>
        """,
        unsafe_allow_html=True
    )

    technique = st.selectbox(
        "Select Prompting Technique",
        techniques
    )

    st.markdown(
        f"""
        <div class="badge">
            ✨ {technique}
        </div>
        """,
        unsafe_allow_html=True
    )

    task = st.text_area(
        "Enter your task",
        placeholder="Example: Explain how React components work.",
        height=180
    )

    st.markdown("### ⚙️ Model Settings")

    temperature = st.slider(
        "🌡️ Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1
    )

    max_tokens = st.slider(
        "📝 Maximum Tokens",
        min_value=100,
        max_value=1000,
        value=500,
        step=100
    )

    st.markdown("</div>", unsafe_allow_html=True)

    generate = st.button("🚀 Generate Response")

with col2:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">💡 Prompting Technique</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="
            color:#e2e8f0;
            font-size:16px;
            line-height:1.7;
        ">
        {descriptions[technique]}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
            <div class="card-title">📊 Current Configuration</div>
        """,
        unsafe_allow_html=True
    )

    config_col1, config_col2 = st.columns(2)

    with config_col1:
        st.metric("Technique", technique)

    with config_col2:
        st.metric("Max Tokens", max_tokens)

    st.markdown("</div>", unsafe_allow_html=True)

if generate:
    if not task.strip():
        st.warning("⚠️ Please enter a task before generating a response.")
    else:
        try:
            prompt = build_prompt(
                technique,
                task
            )

            with st.spinner("🧠 Aura is generating your response..."):
                answer = generate_response(
                    prompt,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

            st.markdown(
                f"""
                <div class="card">
                    <div class="card-title">
                        ✨ Generated Response
                    </div>

                    <div class="badge">
                        {technique}
                    </div>

                    <div class="answer-box">
                        {answer}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            with st.expander("🔍 View Generated Prompt"):
                st.code(
                    prompt,
                    language="text"
                )

        except Exception as e:
            st.error(f"❌ Error: {e}")

st.markdown(
    """
    <div class="footer">
        🤖 Aura Prompt Engineering • Streamlit • Hugging Face
    </div>
    """,
    unsafe_allow_html=True
)