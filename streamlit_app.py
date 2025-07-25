import streamlit as st

from modules.ai_node import handle_ai_node
from actions import label_and_respond_to_issues, close_stale_issues

st.set_page_config(page_title="GitHub AI Automation", layout="wide")
st.title("🤖 GitHub AI Automation Dashboard")
st.markdown("Use the button below to run automation on your GitHub repository.")

with st.expander("🔧 Configuration"):
    st.markdown("Set keywords for issue labeling")
    keywords = st.text_input("Keywords (comma-separated)", value="bug,feature,question")
    st.session_state["keywords"] = [k.strip() for k in keywords.split(",")]

if st.button("🚀 Run Automation"):
    st.success("Executing automation...")

    try:
        handle_ai_node()
        label_and_respond_to_issues()
        close_stale_issues()
        st.success("✅ Automation completed successfully.")
    except Exception as e:
        st.error(f"⚠️ Error during automation: {e}")
