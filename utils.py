import streamlit as st

def logout():
    """Logs the user out and redirects to the Home page."""
    if st.button("Logout", key="logout_button"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.current_page = "Home"  # Redirect to home on logout
        st.rerun()
