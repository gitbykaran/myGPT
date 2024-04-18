import streamlit as st
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from apikey import key
import os

os.environ['OPENAI_API_KEY'] = key


llm = OpenAI(temperature=0.9)

st.title('MY GPT:')
prompt = st.text_input('Enter your prompt here')

if prompt:
    response = llm(prompt)
    st.write(response)
