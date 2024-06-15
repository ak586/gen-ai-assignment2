import streamlit as st
from pages import login, register

# Set the page configuration
st.set_page_config(page_title="Login and Register", page_icon=":key:", layout="centered")

# Load CSS styles
def load_css():
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navigation
pages = {
    "Login": login.show_login_page,
    "Register": register.show_register_page
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page
load_css()
pages[selection]()
