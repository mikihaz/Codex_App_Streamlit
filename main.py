# Importing Libraries
import streamlit as st
import widget

# Making the Streamlit App
header = st.container()
body = st.container()

with header:
  widget.header()

with body:
  widget.body()