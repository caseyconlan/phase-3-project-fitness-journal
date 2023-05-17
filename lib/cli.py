import click
from datetime import datetime
from lib.db import db_session, init_db
from lib.db.models import FitnessLog, ExerciseType

@click.group()
def cli():
    pass

def add_fitness_log():
    init_db()

    date = input("Enter the date (yyyy-mm-dd): ")
    date = datetime.strptime(date, "%Y-%m-%d").date()

    exercise = input("Enter the name of the exercise: ")

    exercise_type = ""
    while exercise_type not in ExerciseType.__members__:
        exercise_type = input("Enter the exercise type ('Strength Training' or 'Cardio'): ")
        exercise_type = exercise_type.replace(" ", "_").upper()

    exercise_type = ExerciseType[exercise_type]

    weight_or_speed = float(input("Enter the weight (in lbs) or speed (in mph): "))
    reps_or_time = int(input("Enter the number of reps or duration (in minutes): "))
    muscle_group = input("Enter the muscle group: ")
    journal_entry = input("Enter any additional notes: ")

    new_log = FitnessLog(date=date, exercise=exercise, exercise_type=exercise_type,
                         weight_or_speed=weight_or_speed, reps_or_time=reps_or_time,
                         muscle_group=muscle_group, journal_entry=journal_entry)
    db_session.add(new_log)
    db_session.commit()

    print("Fitness log added!")

    
@click.command()
def view_fitness_log():
    """View all fitness log entries."""
    logs = db_session.query(FitnessLog).all()
    for log in logs:
        print(f"{log.date} - {log.exercise} - {log.exercise_type.value} - {log.weight_or_speed} - {log.reps_or_time} - {log.muscle_group} - {log.journal_entry}")


if __name__ == "__main__":
    while True:
        print("Welcome to LiftATon!")
        print("❚█══█❚ ❚█══█❚ ❚█══█❚")
        print("1. Add Fitness Log")
        print("2. View Fitness Log")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_fitness_log()
        elif choice == "2":
            view_fitness_log()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
            

