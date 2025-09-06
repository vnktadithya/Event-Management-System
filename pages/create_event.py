import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import Config
from app.models import Event
from datetime import date

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

if "user" not in st.session_state:
    st.session_state.user = None

def create_event():

    if st.session_state.user is None:
        st.warning("Please log in to create an event.")
        return
    
    cols = st.columns([8, 2]) 

    with cols[0]:
        st.title("Create New Event")

    with cols[1]:
        if st.button("Back to Dashboard"):
            st.session_state.current_page = "Home"
            st.switch_page("main.py")


    user = st.session_state.user
    event_name = st.text_input("Event Name")
    event_type = st.selectbox("Event Type", ["Workshop", "Seminar", "Hackathon", "Sports", "Other"])
    date_input = st.date_input("Date", min_value=date.today())
    venue = st.text_input("Venue")
    description = st.text_area("Description")

    if st.button("Create Event"):
        if not event_name or not date_input or not venue:
            st.warning("Please fill in all required fields.")
            return

        new_event = Event(
            event_name=event_name,
            event_type=event_type,
            date=date_input,
            venue=venue,
            organised_by=user.user_id,
            description=description
        )
        session.add(new_event)
        session.commit()
        st.success("Event created successfully!")

create_event()