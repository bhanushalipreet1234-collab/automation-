import streamlit as st

try:
    GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    REPO_NAME = st.secrets["REPO_NAME"]
    KEYWORDS = [kw.strip() for kw in st.secrets["KEYWORDS"].split(",")]
except KeyError as e:
    raise RuntimeError(f"Missing required secret: {e}")
