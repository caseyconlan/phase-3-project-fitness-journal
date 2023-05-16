from helpers import db_session
from db.models import FitnessLog

if __name__ == "__main__":
    while True:
        print("1. Add Fitness Log")
        print("2. View Fitness Log")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Add fitness log entry")
            pass
        elif choice == "2":
            print("View fitness log entries")
            pass
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
