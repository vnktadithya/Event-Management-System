import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, delete
from app.config import Config
from app.models import Event, Register, User

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

if "user" not in st.session_state:
    st.session_state.user = None

def my_events():
    if st.session_state.user is None:
        st.warning("Please log in to view your events.")
        return
    
    cols = st.columns([8, 2])  # Adjust the proportions as needed

    # Add the title to the first column
    with cols[0]:
        st.title("My Events")

    # Add the button to the second column
    with cols[1]:
        if st.button("Back to Dashboard"):
            st.session_state.current_page = "Home"
            st.switch_page("main.py")
    
    user = st.session_state.user

    events = session.query(Event).filter_by(organised_by=user.user_id).all()

    if not events:
        st.info("You haven't created any events yet.")
        return

    for event in events:
        with st.expander(event.event_name):
            st.write(f"Type: {event.event_type}")
            st.write(f"Date: {event.date}")
            st.write(f"Venue: {event.venue}")
            st.write(f"Description: {event.description}")

            # Fetch registered users for the event
            registrations = session.query(Register).filter_by(event_id=event.event_id).all()
            if registrations:
                st.subheader("Registered Users:")
                for registration in registrations:
                    # Get user details from the User table using the user_id in the Registration table.
                    registered_user = session.query(User).filter_by(user_id=registration.user_id).first()
                    if registered_user:
                        st.write(f"- Name: {registered_user.user_name}, Email: {registered_user.email}, Department: {registered_user.dept}")
                    else:
                        st.write("- User details not found") # edge case, if user is deleted.
            else:
                st.write("No users registered for this event yet.")

            if st.button("Delete Event", key=f"delete_event_{event.event_id}"):
                # Use a delete statement
                stmt = delete(Event).where(Event.event_id == event.event_id)
                session.execute(stmt)
                session.commit()
                st.success(f"Event '{event.event_name}' deleted successfully!")
                # Force refresh
                st.rerun()

my_events()