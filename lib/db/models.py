from sqlalchemy import create_engine, Column, Integer, String, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum
from ..helpers import DATABASE_URL

Base = declarative_base()

class ExerciseType(PyEnum):
    CARDIO = "Cardio"
    STRENGTH_TRAINING = "Strength Training"

class MuscleGroup(PyEnum):
    ARMS = "Arms"
    CORE = "Core"
    LEGS = "Legs"
    FULL_BODY = "Full Body"

class FitnessLog(Base):
    __tablename__ = 'fitness_logs'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    exercise = Column(String, nullable=False)
    exercise_type = Column(Enum(ExerciseType), nullable=False)
    weight_or_speed = Column(Integer, nullable=False)
    reps_or_time = Column(Integer, nullable=False)
    muscle_group = Column(Enum(MuscleGroup), nullable=False)
    journal_entry = Column(String, nullable=True)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
