from phi.agent import Agent  , RunResponse  
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
import yfinance as yf
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os
load_dotenv()

openai_key = os.getenv("")
groq_api_key = os.getenv("GROQ_API_KEY")  # Ensure you are getting the correct variable

# Set the API key directly in the Groq initialization

# Create an agent instance
Fady_finance_agent= Agent(
    model =Groq(id ="llama-3.3-70b-versatile",api_key=groq_api_key), 
    #model =OpenAIChat(id ="gpt-4o",api_key=OPENAI_API_KEY),
    tools = [YFinanceTools(stock_price=True ,analyst_recommendations=True,stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Use tables to display data where applicable."
    ]
)

# app.py

import streamlit as st

# Custom Title and Slogan with color
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            color: #4CAF50;  /* Green color for the title */
            font-weight: bold;
        }
        .slogan {
            font-size: 24px;
            color: #FF6347;  /* Tomato color for slogan */
            font-style: italic;
        }
    </style>
    <div class="title">💰Finance Assistant</div>
    <div class="slogan">Get real-time financial insights using my Sample App</div>
""", unsafe_allow_html=True)
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select an option:", ["Ask a Question", "About"], index=0)
    st.markdown("---")
    st.markdown("*Built with Streamlit and AI-powered Agents*")

if page == "Ask a Question":
    st.write("Hello Iam AI-Assistant Please Enter your financial inquery below:")
    user_query = st.text_input("Your question:", "")

    if user_query:
        with st.spinner("Fetching response..."):
            response = Fady_finance_agent.run(user_query)
            clean_response = response.content if hasattr(response, "content") else str(response)

        st.markdown("### Response:")
        st.markdown(clean_response, unsafe_allow_html=True)

# About page content
elif page == "About":
    st.subheader("About this Sample Finance Assistant")
    st.write("""
        This Finance Assistant is an AI-powered tool designed to provide real-time financial insights and information,
        helping users make informed financial decisions. The AI-Assistant is built using Llama and Streamlit. 
        Although this is a sample agent, it reflects how this tool can assist treasury professionals and others in 
        their daily tasks by providing instant real-time data. This allows them to free up time for more critical and 
        strategic decisions.
    """)