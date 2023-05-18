import click
from datetime import datetime
from lib.db import db_session, init_db
from lib.db.models import FitnessLog, ExerciseType, BMI, FoodLog 

@click.group()
def cli():
    pass

def add_fitness_log():
    init_db()

    date = input("Enter the date (mm-dd-yyyy): ")
    date = datetime.strptime(date, "%m-%d-%Y").date()

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

def add_food_log():
    """Allows user to input food data"""
    init_db()


    date = input("Enter the date (mm-dd-yyyy): ")
    date = datetime.strptime(date, "%m-%d-%Y").date()


    food = input("Enter 1 Food Item Name: ")
    calories = input("Enter Number Of Calories in the Food Above(kCal): ")
    journal_entry = input("Enter any additional notes: ")


    new_food_log = FoodLog(date=date, food=food, calories = calories, journal_entry=journal_entry)
    db_session.add(new_food_log)
    db_session.commit()

    print("Food log added!")


@click.command()
def view_food_log():
    """View all food log entries"""
    logs = db_session.query(FoodLog).all()
    for log in logs:
        print(f"{log.date} - {log.food} - {log.calories} - {log.journal_entry}")
    
@click.command()
def view_fitness_log():
    """View all fitness log entries."""
    logs = db_session.query(FitnessLog).all()
    for log in logs:
        print(f"{log.date} - {log.exercise} - {log.exercise_type.value} - {log.weight_or_speed} - {log.reps_or_time} - {log.muscle_group} - {log.journal_entry}")
@click.command()
def sum_calories():
    """Calculates all calories in your calorie row (should sum all calories per date)"""
    # all_calories = for calories in calories
    # sum = len(all_calories)
    # total = sum(calories.all)
    # if date == date:
    #     return "Total Calories on {date} = {total}"

def bmi():
    """Calculates BMI Based On Input"""
    init_db()

    date = input("Enter the date (mm-dd-yyyy): ")
    date = datetime.strptime(date, "%m-%d-%Y").date()

    weight = float(input("Enter your weight (in lbs): "))
    height = float(input("Enter your height (in inches): "))

    # Calculate BMI
    bmi_value = (703 * weight) / (height * height)
    bmi_value = round(bmi_value, 2)

    journal_entry = input("Enter any additional notes: ")

    new_bmi = BMI(date=date, height=height, weight=weight, bmi=bmi_value, journal_entry=journal_entry)
    db_session.add(new_bmi)
    db_session.commit()

    
    #print("❚█══█❚", end=" ")
    print(f"❚█══█❚",f"Your BMI is: {bmi_value}", f"❚█══█❚")
    #print("❚█══█❚")
    

def delete_entry():
    entry_id = int(input("Enter the entry ID to delete: "))
    entry_type = ""
    while entry_type not in ["Fitness", "Food", "BMI"]:
        entry_type = input("Enter the entry type ('Fitness' or 'Food' or 'BMI'): ")

    if entry_type == "Fitness":
        entry = db_session.query(FitnessLog).get(entry_id)
    elif entry_type == "Food":
        entry = db_session.query(FoodLog).get(entry_id)
    elif entry_type == "BMI":
        entry = db_session.query(BMI).get(entry_id)

    if entry:
        db_session.delete(entry)
        db_session.commit()
        click.echo(f"{entry_type} entry with ID {entry_id} has been deleted.")
    else:
        click.echo(f"No {entry_type} entry found with ID {entry_id}.")

print("Welcome to LiftATon!")
print("❚█══█❚ ❚█══█❚ ❚█══█❚")
if __name__ == "__main__":
    while True:
        print("1. Add Fitness Log")
        print("2. View Fitness Log")
        print("3. Add Food & Calories")
        print("4. View Food Log")
        print("5. Total Calories Per Date")
        print("6. Calculate BMI")
        print("7. Delete Entry")
        print("8. Exit")
        print("❚█══█❚ ❚█══█❚ ❚█══█❚")  

        choice = input("Enter your choice: ")

        if choice == "1":
            add_fitness_log()
        elif choice == "2":
            view_fitness_log()
        elif choice == "3":
            add_food_log()
        elif choice == "4":
            view_food_log()
        elif choice == "5":
            sum_calories()
        elif choice == "6":
            bmi()
        elif choice == "7":
            entry_id = int(input("Enter the ID of the entry to delete: "))
            delete_entry(entry_id)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")