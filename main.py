import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import importlib

from app.config import Config

# Import utils normally since it doesn't contain auto-executing functions
from utils import logout

# Setup database engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

# Initialize session state variables if they don't exist
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'user' not in st.session_state:
    st.session_state.user = None

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home" # Default page

# Dictionary of page module paths
page_modules = {
    "Home": "pages.home",
    "Login": "pages.login",
    "Sign Up": "pages.signup",
    "Create Event": "pages.create_event",
    "Register Event": "pages.register_event",
    "My Events": "pages.my_events"
}

# Function to dynamically import page modules and get their main function
def get_page_function(page_name):
    module = importlib.import_module(page_modules[page_name])
    # Get the function with the same name as the module's filename
    function_name = page_modules[page_name].split('.')[-1]
    return getattr(module, function_name)

def show_dashboard():
    # This function shows content when the user is logged in
    user = st.session_state.user
    st.title(f"Welcome to your Dashboard, {user.user_name}!")
    st.write("Here you can manage your events and participation.")

    # Example actions - you'll build these out
    if st.button("View My Events", key="view_my_events_button"):
        st.session_state.current_page = "My Events"
        st.switch_page("pages/my_events.py")

    if st.button("Register for an Event", key="register_for_event_button"):
        st.session_state.current_page = "Register Event"
        st.switch_page("pages/register_event.py")

    if st.button("Create New Event", key="create_new_event_button"):
        st.session_state.current_page = "Create Event"
        st.switch_page("pages/create_event.py")

def main():
    st.sidebar.title("Navigation 🧭")


    if st.session_state.logged_in:
        cols = st.columns([1, 4, 1])  # Adjust the proportions as needed
        with cols[2]:
            logout()
        user = st.session_state.user
        st.sidebar.success(f"Logged in as: {user.user_name}") # Display who is logged in
        page_options = ["Home", "My Events", "Register Event", "Create Event"]

        # Restrict access to login/signup pages when logged in
        if st.session_state.current_page in ["Login", "Sign Up"]:
            st.warning("Please log out to access Login or Sign Up pages.")
            st.session_state.current_page = "Home"  # Keep user on Home page
            st.rerun()

        show_dashboard()

    else:
        # Page selection for non-logged-in users
        page_options = ["Home"]
        
        # Ensure current_page is valid, default to Home
        if st.session_state.current_page not in ["Home", "Login", "Sign Up"]:
            st.session_state.current_page = "Home"

        # Selectively import and call only the current page's function
        current_page = st.session_state.current_page
        try:
            page_function = get_page_function(current_page)
            page_function()  # Call the page function
        except Exception as e:
            st.error(f"Error loading page: {e}")
            st.session_state.current_page = "Home"
            home_function = get_page_function("Home")
            home_function()


if __name__ == '__main__':
    main()