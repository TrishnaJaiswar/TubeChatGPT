import streamlit as st
from dotenv import load_dotenv
from rag import ask_question

load_dotenv()

    
st.title("💬TubeGPT")
st.write("")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if question:
        answer = ask_question(question)
        st.write(answer)



