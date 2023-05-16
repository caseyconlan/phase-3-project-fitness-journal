# The rest of the code remains the same
import requests
from lib.helpers import db_session
from lib.db.models import Base, engine, ExerciseType, MuscleGroup, FitnessLog

Base.metadata.create_all(bind=engine)

exercise_api_url = "https://api-ninjas.com/api/exercises"

response = requests.get(exercise_api_url)
if response.status_code == 200:
    exercises = response.json()

    for exercise in exercises:
        new_log = FitnessLog(
            date = exercise.get('date'),
            exercise = exercise.get('exercise'),
            exercise_type = ExerciseType[exercise.get('exercise_type').upper()],
            weight_or_speed = exercise.get('weight_or_speed'),
            reps_or_time = exercise.get('reps_or_time'),
            muscle_group = MuscleGroup[exercise.get('muscle_group').upper()],
            journal_entry = exercise.get('journal_entry')
        )
        db_session.add(new_log)

    db_session.commit()

else:
    print(f"Error fetching exercises from API. Status Code: {response.status_code}")