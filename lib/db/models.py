from sqlalchemy import Column, Integer, String, Date, Enum
from lib.db import Base
from enum import Enum as PyEnum

class ExerciseType(PyEnum):
    STRENGTH_TRAINING = "Strength Training"
    CARDIO = "Cardio"

class FitnessLog(Base):
    __tablename__ = 'fitness_logs'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    exercise = Column(String(120))
    exercise_type = Column(Enum(ExerciseType))
    weight_or_speed = Column(Integer)
    reps_or_time = Column(Integer)
    muscle_group = Column(String(120))
    journal_entry = Column(String(500))
