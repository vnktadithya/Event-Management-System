import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import Config
from app.models import User
from werkzeug.security import check_password_hash  

# Setup DB
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Initialize state for login failure
if 'login_failed' not in st.session_state:
    st.session_state.login_failed = False

def login():
    st.title("Login")
    email = st.text_input("Email", key="email_input")
    password = st.text_input("Password", type="password", key="password_input")

    if st.button("Login"):
        if not email or not password:
            st.warning("Please enter both email and password.")
        else:
            user = session.query(User).filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                st.session_state.logged_in = True
                st.session_state.user = user
                st.session_state.login_failed = False
                st.switch_page("main.py")
            else:
                st.session_state.login_failed = True
                st.error("Invalid email or password. Please try again.")

    # Only show this button if login failed previously
    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("Don't have an account?")
    with col2:
        if st.button("Sign Up", key = "signup_button"):
            st.session_state.current_page = "Sign Up"
            st.switch_page("pages/signup.py")

login()
