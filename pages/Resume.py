import streamlit as st
from theme_manager import apply_theme

apply_theme()

st.title("📄 Resume")

with open("resume.pdf", "rb") as file:
    st.download_button("📥 Download Resume", file, file_name="Shameer_Asim_Resume.pdf")

st.markdown("---")
st.write("📄 Preview:")
st.file_uploader("Upload a Resume (PDF)", type="pdf")
