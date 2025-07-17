import streamlit as st
from theme_manager import apply_theme

apply_theme()

st.set_page_config(page_title="Social Media", layout="centered")
st.title("🔗 Connect with Me")

st.markdown("""
<style>
.social-card {
    background-color: rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}
.social-card:hover {
    transform: scale(1.03);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
}
.social-icon {
    font-size: 30px;
    margin: 10px;
}
a {
    color: inherit;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='social-card'>
        <a href="https://www.linkedin.com/in/shameer-asim-445612366" target="_blank">
            <span class="social-icon">💼</span><br>
            <strong>LinkedIn</strong>
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='social-card'>
        <a href="https://github.com/ShameerAsim21" target="_blank">
            <span class="social-icon">💻</span><br>
            <strong>GitHub</strong>
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='social-card'>
        <a href="mailto:shameerasim123@gmail.com" target="_blank">
            <span class="social-icon">📧</span><br>
            <strong>Gmail</strong>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='social-card'>
        <a href="https://www.instagram.com/shameer_asim/" target="_blank">
            <span class="social-icon">📸</span><br>
            <strong>Instagram</strong>
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='social-card'>
        <a href="https://www.facebook.com/shameer.asim.90" target="_blank">
            <span class="social-icon">📘</span><br>
            <strong>Facebook</strong>
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='social-card'>
        <a href="mailto:shameerasim21@outlook.com" target="_blank">
            <span class="social-icon">📨</span><br>
            <strong>Outlook</strong>
        </a>
    </div>
    """, unsafe_allow_html=True)
    