import streamlit as st
import smtplib
from db_manager import valid_email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_alert_email(to_email, subject, message, from_email, from_password):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

def forgot_password_page():
    st.title("Forgot Password")
    st.write("Enter your email address to reset your password")
    email = st.text_input("Email")
    if st.button("Reset Password"):
        if valid_email(email):
            subject = 'Password Reset for Crop Recommendation System'
            url='https://password-change-option.streamlit.app/'
            message = f'Click on the link to reset your password: {url}'
            from_email = 'noreply.234878978@gmail.com'
            from_password = 'usyv gsti xpcg rgai'  
    
            # Send the alert email
            send_alert_email(email, subject, message, from_email, from_password)
            st.success("Password reset link has been sent to your email address")
        else:
            st.error("Invalid email address. Please enter a valid email address")
