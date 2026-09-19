import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # local development: reads GROQ_API_KEY from .env


def _get_api_key():
    # 1) Streamlit Cloud: App settings -> Secrets
    try:
        import streamlit as st
        if "GROQ_API_KEY" in st.secrets:
            return str(st.secrets["GROQ_API_KEY"]).strip().strip('"').strip("'")
    except Exception:
        pass  # no secrets file / not running in Streamlit

    # 2) Local: environment variable / .env
    key = os.getenv("GROQ_API_KEY")
    if key:
        return key.strip().strip('"').strip("'")

    raise RuntimeError(
        "GROQ_API_KEY not found. Add it to .env locally, or to "
        "Streamlit Cloud -> Manage app -> Settings -> Secrets."
    )


llm = ChatGroq(
    groq_api_key=_get_api_key(),
    model_name="openai/gpt-oss-120b",
)

if __name__ == "__main__":
    response = llm.invoke("What are the two main ingredients in samosa?")
    print(response.content)
