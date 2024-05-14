import os
import webbrowser
import requests
import streamlit as st
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
st.set_page_config(layout="wide")
st.image('NAU_logo.png', width=600)
st.header('Department of Global Languages and Cultures', divider='rainbow')
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 30px;">Welcome to the Chinese Program!</p>'
st.markdown(new_title, unsafe_allow_html=True)

st.title('🦜🔗 Chatbot')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7)
  st.info(llm(input_text))

text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
generate_response(text)
