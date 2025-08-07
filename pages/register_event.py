import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import Config
from app.models import Event, Register
from datetime import date

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

if "user" not in st.session_state:
    st.session_state.user = None

def register_event():
    if st.session_state.user is None:
        st.warning("Please log in to register for events.")
        return
    
    cols = st.columns([8, 2])  # Adjust the proportions as needed

    # Add the title to the first column
    with cols[0]:
        st.title("Register for Events")

    # Add the button to the second column
    with cols[1]:
        if st.button("Back to Dashboard"):
            st.session_state.current_page = "Home"
            st.switch_page("main.py")
    
    user = st.session_state.user

    events = session.query(Event).filter(Event.date >= date.today()).all()

    if not events:
        st.info("No upcoming events.")
        return

    for event in events:
        with st.expander(event.event_name):
            st.write(f"Type: {event.event_type}")
            st.write(f"Date: {event.date}")
            st.write(f"Venue: {event.venue}")
            st.write(f"Description: {event.description}")

            already_registered = session.query(Register).filter_by(user_id=user.user_id, event_id=event.event_id).first()
            if already_registered:
                st.success("You are already registered.")
            else:
                if st.button(f"Register for {event.event_name}", key=f"register_{event.event_id}"):
                    reg = Register(user_id=user.user_id, event_id=event.event_id, status="Registered", reg_date=date.today())
                    session.add(reg)
                    session.commit()
                    st.success(f"Registered for {event.event_name}")

register_event()