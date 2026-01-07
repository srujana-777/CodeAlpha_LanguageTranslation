#CodeAlpha Task 1: Language Translation Tool

#Author: Srujana

#Description: A simple language translation app using Streamlit and Google Translate API

import streamlit as st 

#Initialize translator
from deep_translator import GoogleTranslator

#App title

st.set_page_config(page_title="Language Translation Tool", page_icon="🌍")
st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages easily")

#Input text

text = st.text_area("Enter text to translate:")

#Language options

languages = { 
    "English": "en", 
    "Hindi": "hi", 
    "Telugu": "te", 
    "Tamil": "ta", 
    "Kannada": "kn", 
    "Malayalam": "ml", 
    "French": "fr", 
    "German": "de", 
    "Spanish": "es" 
}
source_lang = st.selectbox("Select source language", list(languages.keys()))
target_lang = st.selectbox("Select target language", list(languages.keys()))
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        try:
            translated_text = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.success("Translation Successful")
            st.text_area("Translated Text:", translated_text)

        except Exception as e:
            st.error("Translation failed")
            st.write(e)