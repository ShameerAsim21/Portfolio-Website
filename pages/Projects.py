import streamlit as st
from theme_manager import apply_theme

apply_theme()


st.title("📁 Projects")

projects = [
    {
        "title": "Number Guesser Game",
        "description": "Number game where user have to guess a random number chosen by the program.",
        "github": "https://github.com/ShameerAsim21/Number-Guesser-Game.git"
    },
    {
        "title": "Temperature Converter App",
        "description": "Converts the temperature within Kelvin, Farenheit or Celsius",
        "github": "https://github.com/ShameerAsim21/Temperature-Convertor.git"
    },
    {
        "title": "Attendence Management App",
        "description": "Two seperate apps (Teacher App & Student App) to manage the attendence easily",
        "github": "https://github.com/ShameerAsim21/Attendance-Management-App.git"
    },
    {
        "title": "Sudoku Solver",
        "description": "Takes user's input and solves the sudoku puzzle if possible",
        "github": "https://github.com/ShameerAsim21/Sudoku-Solver.git"
    },
    {
        "title": "Maze Game",
        "description": "A maze game with different obstacles and timer.",
        "github": "https://github.com/ShameerAsim21/Maze-Game.git"
    },
    {
        "title": "Currency Converter App",
        "description": "Converts the given amount into the required currency",
        "github": "https://github.com/ShameerAsim21/Currency-Converter-App.git"
    },
    {
        "title": "Voice Dictionary App",
        "description": "Dictonary with text to speech features",
        "github": "https://github.com/ShameerAsim21/Voice-Dictionary.git"
    },
    {
        "title": "Mood Detection App",
        "description": "Detects user's mood via webcam and plays suitable music.",
        "github": "https://github.com/ShameerAsim21/Mood-Detection-App.git"
    },
    {
        "title": "Resume Ranker",
        "description": "Ranks resumes based on job description using NLP.",
        "github": "https://github.com/ShameerAsim21/Resume-Ranker.git"
    }
]

for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
    st.markdown(f"[🔗 GitHub]({project['github']})")
    st.markdown("---")
