import streamlit as st
import time

# Page config
st.set_page_config(page_title="My Portfolio", page_icon="🌲", layout="wide")

# Custom CSS for dark green theme and full-screen styling
st.markdown(
    """
    <style>
        body {
            background-color: #2e371a;
            color: #e0e0e0;
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background-color: #4a5931;
            color: white;
            border-radius: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Background audio (rain sounds)
st.markdown(
    """
    <audio autoplay loop>
        <source src="https://www.soundjay.com/nature/rain-01.mp3" type="audio/mpeg">
    </audio>
    """,
    unsafe_allow_html=True,
)

# Header
st.title("🌲 Welcome to My Portfolio")
st.write("A cozy, minimalist portfolio inspired by mountain vibes.")

# Sections
st.header("About Me")
st.write("I'm a developer passionate about AI, C++, and system design.")

st.header("Projects")
st.write("- **AI Agent**: Building an AI-powered assistant using gRPC & WASM.")
st.write("- **Compiler Optimizer**: AI-driven compiler optimizer for C++.")
st.write("- **Supply Chain Dashboard**: AI-powered project tracking tool.")

st.header("Contact")
st.write("📧 Email: your.email@example.com")
st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile)")
st.write("💻 [GitHub](https://github.com/yourusername)")
