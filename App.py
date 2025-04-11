from phi.agent import Agent  , RunResponse  
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
import yfinance as yf
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os
load_dotenv()

openai_key = os.getenv("")

# Set the API key directly in the Groq initialization

# Create an agent instance
Fady_finance_agent= Agent(
    model =Groq(id ="llama-3.3-70b-versatile",api_key=os.getenv("GROQ_API_KEY")), 
    #model =OpenAIChat(id ="gpt-4o",api_key=OPENAI_API_KEY),
    tools = [YFinanceTools(stock_price=True ,analyst_recommendations=True,stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Use tables to display data where applicable."
    ]
)

Fady_finance_agent.print_response("WHAT IS TREASURY MANAGEMENT")

# app.py

import streamlit as st

st.set_page_config(page_title="Finance Assistant", page_icon="💰", layout="wide")
st.title("💰 Fady Finance Assistant")
st.markdown("### Get real-time financial insights and web-based information")

with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select an option:", ["Ask a Question", "About"], index=0)
    st.markdown("---")
    st.markdown("*Built with Streamlit and AI-powered Agents*")

if page == "Ask a Question":
    st.write("Enter your financial or web-related query below:")
    user_query = st.text_input("Your question:", "")

    if user_query:
        with st.spinner("Fetching response..."):
            response = Fady_finance_agent.run(user_query)
            clean_response = response.content if hasattr(response, "content") else str(response)

        st.markdown("### Response:")
        st.markdown(clean_response, unsafe_allow_html=True)

elif page == "About":
    st.subheader("About Finance Assistant")
    st.write("Finance Assistant is an AI-powered tool designed to provide real-time financial insights and web-based information.")
