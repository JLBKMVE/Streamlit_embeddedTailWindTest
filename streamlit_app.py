import streamlit as st
from streamlit.components.v1 import html
from pathlib import Path

st.set_page_config(page_title="Embedded Next.js/Tailwind Dashboard", layout="wide")
st.title("Embedded Next.js/Tailwind Dashboard")

dashboard_path = Path(__file__).with_name("dashboard.html")
if dashboard_path.exists():
    html(dashboard_path.read_text(encoding="utf-8"), height=900, scrolling=True)
else:
    st.error("dashboard.html not found")