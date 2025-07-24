# streamlit_app.py

import streamlit as st
from actions import label_and_respond_to_issues, close_stale_issues

st.title("🤖 GitHub AI Automation Bot")
st.write("Run issue labeling, response, and stale issue cleanup.")

if st.button("Run Automation Now"):
    st.info("Running bot...")
    try:
        label_and_respond_to_issues()
        close_stale_issues()
        st.success("Bot run complete!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
