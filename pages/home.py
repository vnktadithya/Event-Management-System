import streamlit as st

def home():
    st.title("Welcome to the College Event Portal 🎉")
    st.write("""
        Your one-stop platform for discovering, managing, and participating in college events.
        
        **For Students:**
        -   Explore a wide range of events, from academic workshops to social gatherings.
        -   Easily register for events that interest you.
        -   Stay updated with event schedules and important announcements.
        -   Connect with other students and expand your network.
        -   Provide feedback and ratings for events you've attended.

        **For Event Organizers:**
        -   Create and manage events with ease.
        -   Promote your events to the college community.
        -   Track registrations and manage attendees.
        -   Communicate with participants and share updates.
    
        **Key Features:**
        -   Event Listings: Browse events by category, date, and location.
        -   Registration: Simple and secure event registration process.
        -   User Profiles: Manage your profile and event participation.
        -   Notifications: Stay informed about upcoming events and changes.
        -   Feedback and Ratings: Share your experience and help improve events.
             
    """)

    if st.button("Get Started", key="get_button"):
        st.session_state.current_page = "Sign Up"
        st.switch_page("pages/signup.py")
