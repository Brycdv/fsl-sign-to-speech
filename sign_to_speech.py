import streamlit as st
import pyttsx3
import random

# Placeholder for sign recognition (extended for full Filipino Sign Language alphabet and numbers)
signs = {
    "A": "Ako", "B": "Bahay", "C": "Cebu", "D": "Dagat", "E": "Elepante", "F": "Filipino",
    "G": "Gatas", "H": "Hangin", "I": "Isda", "J": "Juice", "K": "Kaibigan",
    "L": "Laro", "M": "Mahal", "N": "Nanay", "O": "Oras", "P": "Pamilya",
    "Q": "Quatro", "R": "Radyo", "S": "Sama-sama", "T": "Tubig", "U": "Ulan",
    "V": "Victory", "W": "Wika", "X": "Xylo", "Y": "Yelo", "Z": "Zoo",
    "1": "Isa", "2": "Dalawa", "3": "Tatlo", "oo": "Oo", "hindi": "Hindi",
    "salamat": "Salamat", "kumusta": "Kumusta"
}

# AI-generated background descriptions
themes = {key: f"A background representing '{value}'." for key, value in signs.items()}

# Text-to-Speech function with Filipino voice
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Filipino" in voice.name or "Tagalog" in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

st.title("Filipino Sign Language to Text & Speech")
selected_sign = st.selectbox("Choose a Sign:", list(signs.keys()))

if selected_sign:
    text_output = signs[selected_sign]
    st.write(f"**Recognized Sign:** {selected_sign}")
    st.write(f"**Converted Text:** {text_output}")
    
    # AI-generated background
    theme = themes.get(selected_sign, "A relevant background based on the sign.")
    st.write(f"**AI-Generated Background:** {theme}")
    
    # User input for custom text
    custom_text = st.text_input("Enter your text:", value=text_output)
    
    # Button to trigger speech
    if st.button("Speak"):
        speak(custom_text)
        st.success("Spoken: " + custom_text)