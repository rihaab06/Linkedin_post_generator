import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model_name="openai/gpt-oss-120b"
)
