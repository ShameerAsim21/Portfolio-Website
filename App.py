import streamlit as st
from PIL import Image
from theme_manager import apply_theme
from PIL import Image

# Theme selector – shown only on main app
if "theme" not in st.session_state:
    st.session_state.theme = "Light"

selected = st.sidebar.radio("🌗 Theme", ["Light", "Dark"], 
                            index=0 if st.session_state.theme == "Light" else 1)
st.session_state.theme = selected

apply_theme()

st.set_page_config(page_title="My Portfolio", layout="wide")
st.title(" Welcome to My Portfolio")

# Load profile image
profile_img = Image.open("assets/profile.jpg")

col1, col2 = st.columns([1, 2])
with col1:
    st.image(profile_img, width=200)

with col2:
    st.subheader("Hi, I'm Shameer Asim")
    st.write("""
    I'm a passionate Computer Science student with a focus on Python and AI. 
    I love building smart, intuitive applications and learning new technologies.
    """)
    st.markdown("📚 **Education**: B.S. in Computer Science, Sindh University, Jamshoro")
    st.markdown("🛠️ **Skills**: Python, Streamlit, SQL, Github, OpenCV, MS Office, Adobe Illustrator")

st.markdown("---")
st.write("💡 _“The best design is the simplest one that works. - Albert Einstein ”_")
#run using: 
# python -m streamlit run App.py
