import streamlit as st
def forgot_password_page():
    st.title("Forgot Password")
    st.write("Enter your email address to reset your password")
    email = st.text_input("Email")
    st.button("Reset Password")