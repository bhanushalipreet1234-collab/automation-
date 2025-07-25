import streamlit as st

# Safe import for drawflow
try:
    from streamlit_drawflow import drawflow
    drawflow_available = True
except ImportError:
    drawflow_available = False
    st.warning("⚠️ streamlit-drawflow is not installed.")

from modules.ai_node import handle_ai_node
from actions import label_and_respond_to_issues, close_stale_issues

st.set_page_config(page_title="GitHub AI Automation", layout="wide")
st.title("🤖 GitHub AI Automation Dashboard")
st.markdown("Drag and connect modules to build an automation.")

if drawflow_available:
    data = drawflow(key="flow_editor")
else:
    data = None
    st.info("Run automation using buttons below.")

if st.button("🚀 Run Automation"):
    st.success("Executing automation flow...")

    try:
        handle_ai_node()
        label_and_respond_to_issues()
        close_stale_issues()
        st.success("✅ Automation completed.")
    except Exception as e:
        st.error(f"⚠️ Error during automation: {e}")

if data:
    st.subheader("📊 Flow Output:")
    st.json(data)
