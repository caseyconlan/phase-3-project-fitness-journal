from getpass import getpass
from lib.db import db_session
from lib.db.models import User
import hashlib

def register_user():
    username = input("Enter a username: ")
    password = getpass("Enter a password: ")
    confirm_password = getpass("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    # Hash the password for storing in the database
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = User(username=username, password=hashed_password)
    db_session.add(user)
    db_session.commit()
    print(f"User {username} has been registered successfully!")

def login_user():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    # Hash the entered password to compare with the stored one
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = db_session.query(User).filter(User.username == username).first()
    if user and user.password == hashed_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False
