from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


### logics

model = genai.GenerativeModel("gemini-pro")
def get_ideas(query) -> None:
    response = model.generate_content(query)
    return response.text

### Streamlit for UI
st.set_page_config(page_title="Smartbot")

st.header("Tanishq Smart Bot")

input = st.text_input("Input: ", key = "input")
submit = st.button("Ask the Question")

if submit:
    response = get_ideas(input)
    st.subheader("Your Answer is")
    st.write(response)
