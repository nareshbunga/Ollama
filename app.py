
import streamlit as st
from ollama import Client


# =========================================================
# Page Configuration
# =========================================================
st.set_page_config(
    page_title="Ollama AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# =========================================================
# Ollama Client
# =========================================================
client = Client(host="http://localhost:11434")


# =========================================================
# Custom CSS
# =========================================================
st.markdown(
    """
    <style>

    /* Main container */
    .block-container {
        max-width: 900px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Application title */
    .app-title {
        text-align: center;
        font-size: 2.6rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    /* Subtitle */
    .app-subtitle {
        text-align: center;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    /* Section titles */
    .section-title {
        font-size: 1.15rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }

    /* Selected model */
    .selected-model {
        text-align: center;
        font-size: 0.9rem;
        margin-top: 0.5rem;
        margin-bottom: 1.5rem;
    }

    /* Response heading */
    .response-header {
        font-size: 1.25rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-top: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Application Header
# =========================================================
st.markdown(
    '<div class="app-title">🤖 Ollama AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="app-subtitle">
        Interact with locally hosted Large Language Models using Ollama.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Model Selection
# =========================================================
st.markdown(
    '<div class="section-title">Select a Language Model</div>',
    unsafe_allow_html=True
)

selected_model = st.radio(
    "Available Ollama Models",
    [
        "deepseek-r1:1.5b",
        "llama3.2:latest",
        "gemma3:270m"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown(
    f"""
    <div class="selected-model">
        Selected model: <b>{selected_model}</b>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Prompt Input
# =========================================================
st.markdown(
    '<div class="section-title">Enter Your Prompt</div>',
    unsafe_allow_html=True
)

prompt = st.text_area(
    "Prompt",
    placeholder=(
        "Ask anything... For example: "
        "Explain Retrieval-Augmented Generation (RAG) in simple terms."
    ),
    height=180,
    label_visibility="collapsed"
)


# =========================================================
# Generate Response Button
# =========================================================
generate_button = st.button(
    "🚀 Generate Response",
    use_container_width=True
)


# =========================================================
# Generate LLM Response
# =========================================================
if generate_button:

    # Validate prompt
    if not prompt.strip():

        st.warning(
            "Please enter a prompt before generating a response."
        )

    else:

        try:

            with st.spinner(
                f"Generating response using {selected_model}..."
            ):

                response = client.chat(
                    model=selected_model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

            # -------------------------------------------------
            # Response Section
            # -------------------------------------------------
            st.markdown(
                '<div class="response-header">🤖 AI Response</div>',
                unsafe_allow_html=True
            )

            st.caption(
                f"Generated using **{selected_model}**"
            )

            st.divider()

            st.markdown(
                response["message"]["content"]
            )

        except Exception as e:

            st.error(
                "Unable to generate the response."
            )

            st.info(
                "Please make sure Ollama is running and "
                "the selected model is installed."
            )

            st.caption(
                f"Error details: {e}"
            )


# =========================================================
# Footer
# =========================================================
st.markdown(
    """
    <div class="footer">
        Built with Streamlit & Ollama
    </div>
    """,
    unsafe_allow_html=True
)
