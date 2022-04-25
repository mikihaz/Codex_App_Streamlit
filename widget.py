from time import sleep
import streamlit as st
import config
import codex

def logInForm():
  st.subheader('Log In')
  username = st.text_input('Username')
  password = st.text_input('Password', type='password')
  st.button('Login', on_click=lambda: login(username, password))
  # with st.form("login_form",clear_on_submit = True):
  #   st.subheader("LogIn")
  #   username = st.text_input("Username")
  #   password = st.text_input("Password", type="password")
  #   submitted = st.form_submit_button("Login")
  #   if submitted:
  #     login(username, password)

def login(username, password):
  if username in config.loginCredentials['profiles'].keys():
    if config.loginCredentials['profiles'][username]['password'] == password:
      st.success("Login Successful")
      st.session_state['loginState'] = True
      st.session_state['username'] = config.loginCredentials['profiles'][username]['username']
      # sleep(1.5)
    else:
        st.error("Incorrect Password for " + username)
  else:
    st.error("Login Failed, Please try again with correct credentials")

def logout():
  st.session_state['loginState'] = False
  st.session_state['username'] = False
  # header()
  st.success("Logout Successful")

def header():
  st.title('Force-Py Codex v1.0') # Title of the App
  st.subheader('Your Personal AI Python Coder')
  st.caption('Powered by OpenAI and Force Power Infotech')
  st.caption('Developed by: mikih@z')
  if 'loginState' not in st.session_state or not st.session_state['loginState']:
    st.session_state['loginState'] = False
    logInForm()
  elif 'loginState' in st.session_state:
    col1, col2 = st.columns(2)

    with col1:
      st.text('You are logged in as: ' + config.loginCredentials['profiles'][st.session_state['username']]['name'])

    with col2:
      st.button('Logout', on_click=lambda: logout())
    st.markdown("""---""")

def body():
  if st.session_state.loginState:
    input_text = st.text_input('Write your idea here', help=
    """
    1. Create a list of first names
    2. Create a list of last names
    3. Combine them randomly into a list of 100 full names
    """
   )
    if st.button('Send'):
      with st.spinner('Force-Py Codex is coding your idea...'):
        reply_text = codex.response(input_text)
      st.code(reply_text, language='python')