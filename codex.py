import openai
import config
import streamlit as st

# Assigning the API key
# openai.api_key = config.api_key

# Defining the function to get the output from the model
def response(input_text):
    openai.api_key = config.loginCredentials['profiles'][st.session_state['username']]['api_key']
    reply = openai.Completion.create(
        engine="code-davinci-002",
        prompt="''''\n" + input_text + "\n''''",
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    return reply.choices[0].text