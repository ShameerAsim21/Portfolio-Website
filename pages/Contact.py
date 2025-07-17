import streamlit as st
import pandas as pd
from datetime import datetime
from theme_manager import apply_theme

apply_theme()


st.title("📬 Contact Me")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Send")

    if submitted:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df = pd.DataFrame([[timestamp, name, email, message]],
                          columns=["Timestamp", "Name", "Email", "Message"])
        df.to_csv("messages.csv", mode="a", header=False, index=False)
        st.success("✅ Thank you! Your message has been sent.")
