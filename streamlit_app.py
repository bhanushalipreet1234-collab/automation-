import streamlit as st
from streamlit_drawflow import drawflow
from modules.ai_node import handle_ai_node
from modules.github_node import handle_github_issue
from modules.automation_engine import execute_flow

st.set_page_config(page_title="AI Automation Builder", layout="wide")
st.title("🤖 Visual AI + GitHub Automation Builder")

st.markdown("Drag and connect modules to build an automation.")

data = drawflow(key="flow_editor")

if st.button("🚀 Run Automation"):
    st.success("Executing automation flow...")
    execute_flow(data)
