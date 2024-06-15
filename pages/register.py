import streamlit as st

# Helper function for email validation
def is_valid_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Helper function for password strength validation
def is_strong_password(password):
    return len(password) >= 6  # Add more checks for complexity if needed

def show_register_page():
    st.title("Register")
    with st.form("register_form"):
        st.write('<div class="form-container">', unsafe_allow_html=True)
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit = st.form_submit_button("Register")
        st.write('</div>', unsafe_allow_html=True)

        if submit:
            if not first_name or not last_name:
                st.error("Please enter your first and last name")
            elif not is_valid_email(email):
                st.error("Invalid email format")
            elif not is_strong_password(password):
                st.error("Password too weak")
            elif password != confirm_password:
                st.error("Passwords do not match")
            else:
                st.success("Registration successful")
