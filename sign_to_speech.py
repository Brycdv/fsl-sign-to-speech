import streamlit as st
from gtts import gTTS
import os
import tempfile
import pygame  # For immediate audio playback

# Initialize Pygame Mixer for playing audio
pygame.mixer.init()

# Filipino Sign Language signs and corresponding words
signs = {
    "Select a Sign": "",  # Default placeholder
    "A": "Ako", "B": "Bahay", "C": "Cebu", "D": "Dagat", "E": "Elepante", "F": "Filipino",
    "G": "Gatas", "H": "Hangin", "I": "Isda", "J": "Juice", "K": "Kaibigan",
    "L": "Laro", "M": "Mahal", "N": "Nanay", "O": "Oras", "P": "Pamilya",
    "Q": "Quatro", "R": "Radyo", "S": "Sama-sama", "T": "Tubig", "U": "Ulan",
    "V": "Victory", "W": "Wika", "X": "Xylo", "Y": "Yelo", "Z": "Zoo",
    "1": "Isa", "2": "Dalawa", "3": "Tatlo", "oo": "Oo", "hindi": "Hindi",
    "salamat": "Salamat", "kumusta": "Kumusta"
}

# AI-generated background descriptions
themes = {key: f"A background representing '{value}'." for key, value in signs.items() if key != "Select a Sign"}

# Function to convert text to speech and play immediately
def speak(text):
    try:
        if not text.strip():
            st.warning("Please enter some text before playing.")
            return None

        # Generate speech using gTTS
        tts = gTTS(text=text, lang="tl")  # "tl" for Filipino/Tagalog

        # Save to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_filename = temp_audio.name
            tts.save(temp_filename)

        # Play the generated speech immediately using pygame
        pygame.mixer.music.load(temp_filename)
        pygame.mixer.music.play()

        return temp_filename  # Return the file path
    except Exception as e:
        st.error(f"Error generating speech: {e}")
        return None

# Streamlit UI
st.title("Filipino Sign Language to Text & Speech")

# Select a sign
selected_sign = st.selectbox("Choose a Sign:", list(signs.keys()))

# Ensure selected_sign is valid before using it
if selected_sign and selected_sign != "Select a Sign":
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
        audio_file = speak(custom_text)
        if audio_file:
            st.success(f"Spoken: {custom_text}")

            # Optional: Provide a download button for the speech file
            with open(audio_file, "rb") as f:
                st.download_button("Download Speech", f, file_name="speech.mp3", mime="audio/mp3")
