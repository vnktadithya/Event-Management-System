import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from app.config import Config
from app.models import User
from werkzeug.security import generate_password_hash # For hashing passwords

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def signup():
    st.title("Sign Up")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    dept = st.text_input("Department")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if not name or not email or not password or not confirm_password or not dept:
            st.warning("Please fill all fields.")
            return

        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            st.error("User with this email already exists. Please login.")
            return

        try:
            hashed_password = generate_password_hash(password)
            new_user = User(user_name=name, email=email, password=hashed_password, dept=dept)
            session.add(new_user)
            session.commit()
            st.success("Registration successful! Please proceed to Login.")
            st.balloons()
        except IntegrityError:
            session.rollback()
            st.error("Registration failed due to a database error. Please try again.")
        except Exception as e:
            session.rollback()
            st.error(f"An unexpected error occurred: {e}")

    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("Already have an account?")
    with col2:
        if st.button("Login", key = "login_button"):
            st.session_state.current_page = "Login"
            st.switch_page("pages/login.py")

signup()