Digital Portfolio Website (Streamlit Project)

This is a multi-page personal portfolio website built using Python and Streamlit.
It includes custom themes, a resume viewer, contact form and social media links
making it a complete interactive portfolio to showcase your skills and projects.

──────────────────────────────────────────────
FEATURES
──────────────────────────────────────────────

🏠 Home Page
- Profile picture, personal intro, education, and core skills
- Theme toggle (Light / Dark)
- Responsive layout

💼 Projects Page
- Cards displaying project title, description, tech/tools used, GitHub/demo link

📄 Resume Page
- Download resume (PDF)
- Upload and preview resume inline

📬 Contact Form
- Name, Email, Message fields
- Stores form data in messages.csv
- Shows success message on submission

🌐 Social Media Page
- Links to:
  - LinkedIn
  - GitHub
  - Instagram
  - Facebook
  - Gmail
  - Outlook
──────────────────────────────────────────────

🌗 THEME SUPPORT

✅ Theme toggle in the sidebar (Light / Dark)
✅ Applies to all pages using session_state
✅ Custom styles via HTML/CSS in theme_manager.py

──────────────────────────────────────────────

📁 PROJECT STRUCTURE

portfolio_website/
├── app.py                     → Home page & theme selector
├── theme_manager.py          → Applies selected theme across app
├── resume.pdf                → Your downloadable resume
├── messages.csv              → Form data saved here (auto-created)
├── assets/                   → Images/icons if needed
└── pages/
    ├── 1_Projects.py
    ├── 2_Resume.py
    ├── 3_Contact.py
    └── 4_Social_Media.py

──────────────────────────────────────────────

🛠 TECH USED

- Python 3.10+
- Streamlit
- Pandas
- HTML / CSS (for styling cards, themes, and layout)

──────────────────────────────────────────────

🔧 HOW TO RUN LOCALLY

1. Clone the repository or extract project ZIP
2. Install required packages:

   pip install -r requirements.txt

3. Run the app:

    python -m streamlit run App.py
──────────────────────────────────────────────

✅ FILES 

1. Source Code (all .py files, folders, images)
2. resume.pdf
3. requirements.txt
4. README.txt
──────────────────────────────────────────────

📫 CONTACT

Gmail: shameerasim123@gmail.com  
Outlook: shameerasim21@outlook.com  
LinkedIn: www.linkedin.com/in/shameer-asim-445612366  
GitHub: https://github.com/ShameerAsim21  
Instagram: https://www.instagram.com/shameer_asim/  
Facebook: https://www.facebook.com/shameer.asim.90  

──────────────────────────────────────────────

📝 Internship Task 13 — By Muhammad Shameer Asim