# theme_manager.py

import streamlit as st

def apply_theme():
    theme = st.session_state.get("theme", "Light")

    if theme == "Dark":
        st.markdown("""
            <style>
                .stApp { background-color: #0e1117; color: #fafafa; }
                a { color: #1faee9; }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                .stApp { background-color: #ffffff; color: #000000; }
                a { color: #1f77b4; }
            </style>
        """, unsafe_allow_html=True)
