# config.py

import streamlit as st
import openai

# Load secrets from Streamlit's .streamlit/secrets.toml or cloud secrets manager
try:
    GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
    REPO_NAME = st.secrets["REPO_NAME"]
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    KEYWORDS = st.secrets.get("KEYWORDS", ["bug", "help", "question"])  # default keywords if not set
except KeyError as e:
    raise RuntimeError(f"Missing required secret: {e}")

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY
