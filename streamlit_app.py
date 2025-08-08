import streamlit as st
from streamlit.components.v1 import html
from pathlib import Path

st.set_page_config(
    page_title="Embedded Next.js/Tailwind Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.title("Embedded Next.js/Tailwind Dashboard")

# Use full-width content area inside Streamlit
st.markdown(
    """
    <style>
    .block-container { max-width: 100% !important; padding-left: 0; padding-right: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

dashboard_path = Path(__file__).with_name("dashboard.html")
if dashboard_path.exists():
    html(dashboard_path.read_text(encoding="utf-8"), height=900, scrolling=True)
else:
    st.error("dashboard.html not found")