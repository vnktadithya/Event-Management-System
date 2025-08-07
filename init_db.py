# init_db.py (or your existing script name)
from app.models import Base
from sqlalchemy import create_engine
from app.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

def create_database():
    print("Creating database tables...")
    Base.metadata.create_all(engine)
    print("Database tables created successfully (if they didn't exist).")

if __name__ == '__main__':
    # Optional: For SQLite, you might want to delete the old DB file first
    # import os
    # if os.path.exists("event_db.sqlite3"): # Check if using default SQLite name
    #     print("Deleting old SQLite database file...")
    #     os.remove("event_db.sqlite3")
    create_database()