from ..helpers import db_session
from .models import Base, engine, ExerciseType, MuscleGroup, FitnessLog
from datetime import datetime


Base.metadata.create_all(bind=engine)

exercises = [
    {
        'date': '2023-05-10',
        'exercise': 'Kettlebell Swings',
        'exercise_type': 'STRENGTH_TRAINING',
        'weight_or_speed': 16,
        'reps_or_time': 20,
        'muscle_group': 'FULL_BODY',
        'journal_entry': 'Felt good during the workout.'
    },
    {
        'date': '2023-05-11',
        'exercise': 'Treadmill',
        'exercise_type': 'CARDIO',
        'weight_or_speed': 8,
        'reps_or_time': 30,
        'muscle_group': 'LEGS',
        'journal_entry': 'Nice and steady pace.'
    }
]

for exercise in exercises:
    new_log = FitnessLog(
        date=exercise.get('date'),
        exercise=exercise.get('exercise'),
        exercise_type=ExerciseType[exercise.get('exercise_type').upper()],
        weight_or_speed=exercise.get('weight_or_speed'),
        reps_or_time=exercise.get('reps_or_time'),
        muscle_group=MuscleGroup[exercise.get('muscle_group').upper()],
        journal_entry=exercise.get('journal_entry')
    )
    db_session.add(new_log)

db_session.commit()
