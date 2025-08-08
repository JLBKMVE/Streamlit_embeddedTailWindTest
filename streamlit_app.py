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
    /* Older and newer Streamlit layouts */
    .block-container { max-width: 100% !important; padding-left: 0 !important; padding-right: 0 !important; }
    div[data-testid="stAppViewContainer"] > .main { max-width: 100% !important; padding-left: 0 !important; padding-right: 0 !important; }
    div[data-testid="stMain"] { max-width: 100% !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

dashboard_path = Path(__file__).with_name("dashboard.html")
if dashboard_path.exists():
    html(
        dashboard_path.read_text(encoding="utf-8"),
        height=900,
        width=1200,  # ensure wide iframe; container CSS above lets it breathe
        scrolling=True,
    )
else:
    st.error("dashboard.html not found")