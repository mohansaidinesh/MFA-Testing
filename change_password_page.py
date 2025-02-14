import streamlit as st
import pandas as pd
from db_manager import valid_email,update_password
email=st.text_input('Email')
password=st.text_input('Password',type='password')
confirm_password=st.text_input('Confirm Password',type='password')

if st.button('Change Password'):
    try:
        if valid_email(email):
            if password==confirm_password:
                update_password(email,password)
                st.success('Password Changed Successfully')
            else:
                st.error('Password and Confirm Password should be same')
    except Exception as e:
        st.error(e)
        