import streamlit as st
import os

# 로컬: .env 파일
# Streamlit Cloud: st.secrets
openai_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_key