import streamlit as st

# Helper function for email validation
def is_valid_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Helper function for password strength validation
def is_strong_password(password):
    return len(password) >= 6  # Add more checks for complexity if needed

def show_login_page():
    st.title("Login")
    with st.form("login_form"):
        st.write('<div class="form-container">', unsafe_allow_html=True)
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        st.write('</div>', unsafe_allow_html=True)

        if submit:
            if not is_valid_email(email):
                st.error("Invalid email format")
            elif not is_strong_password(password):
                st.error("Password too weak")
            else:
                st.success("Login successful")
