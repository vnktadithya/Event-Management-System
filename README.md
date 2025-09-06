#  Event Management System

A Streamlit-powered application to create, manage, and participate in college events.

## 📖 Overview

The Event Management System is designed to simplify the organization and participation of college events. It enables students and organizers to discover, register, manage, and track events in a seamless and interactive way.

Built with Streamlit and SQLAlchemy, this system ensures a user-friendly interface for students while giving event organizers the ability to efficiently manage their events and participants.

## ✨ Features

### 👩‍🎓 For Students

* Browse and explore upcoming events by type, date, and venue.
* Register for events in a simple and secure manner.
* View all the events you have registered for.
* Provide feedback and ratings for attended events.
* Manage personal profiles and participation.

### 🎤 For Event Organizers
* Create and manage new events with all details (name, date, venue, description).
* Track event registrations and view participant details.
* Manage and delete existing events.
* Collect feedback to improve future events.

### 🛠️ Core Functionality
* Event Listings – Filter and explore events.
* Registration System – Secure event registration and status tracking.
* User Authentication – Sign up, log in, and manage user sessions.
* Event Feedback – Collect ratings and comments.
* Dashboard – Personalized dashboard for both participants and organizers.

## ⚙️ Installation

To get the Event Management System running on your local machine, follow these steps:

**🔑 Prerequisites**

* Python 3.8+
* `pip` (Python package installer)

**📦 Install Dependencies**

Navigate to the project's root directory in your terminal and use the following command to install the required packages:

    pip install -r requirements.txt

**🗄️ Initialize the Database**

Run the following command to create the database and tables automatically:

    python init_db.py

This will generate a SQLite database (`event_db.sqlite3`) in the project directory.

## 🚀 Usage

To start the application, run the following command in your terminal from the project's root directory:

    streamlit run main.py

**Workflow:**

**1. Home Page:** – Browse all available events or choose to sign up/login.

**2. Sign Up/Login:** – Create a new account or log in to an existing one to access personalized features.

**3. Dashboard:** – After logging in, you will be directed to your dashboard.

  * Students can see upcoming events and register for them.
  * Organizers can create new events and view the events they have created.

**4. My Events:** – This section is for organizers to track participants and manage the events they have created.

**5. Feedback:** – After attending an event, users can provide feedback and ratings.

## 🏗️ Project Structure

    Event-Management-System/
    ├── app/
    │   ├── config.py
    │   ├── models.py
    │
    ├── pages/
    │   ├── home.py
    │   ├── login.py
    │   ├── signup.py
    │   ├── create_event.py
    │   ├── register_event.py
    │   ├── my_events.py
    │
    ├── init_db.py
    ├── main.py
    ├── utils.py
    └── requirements.txt

* **main.py:** The main entry point for the Streamlit application.
* **init_db.py:** A script to initialize the database tables.
* **utils.py:** Contains utility functions, such as logout handling.
* **requirements.txt:** Lists all Python dependencies required for the project.
* **app/:** Contains core application logic and configuration.
    * **config.py:** Handles database configuration.
    * **models.py:** Defines the SQLAlchemy models (User, Event, Register, etc.).
* **pages/:** Directory containing the different pages of the Streamlit application.
    * **home.py:** The welcome/landing page.
    * **login.py & signup.py:** Manages user authentication.
    * **create_event.py:** The form for organizers to create a new event.
    * **register_event.py:** The page for students to register for an event.
    * **my_events.py:** The dashboard for organizers to view and manage their created events.

## 🛠️ Tech Stack

* **Frontend/UI**: Streamlit
* **Backend**: Python + SQLAlchemy
* **Database**: SQLite
* **Authentication**: Secure password hashing with Werkzeug
