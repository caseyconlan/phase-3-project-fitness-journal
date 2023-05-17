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

class FoodLog(Base):
    __tablename__ = 'food_logs'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    food = Column(String(120))
    calories = Column(Integer)
    journal_entry = Column(String(500))


class BMI(Base):
    # https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html#Interpreted
    """Formula: weight (lb) / [height (in)]2 x 703"""
    __tablename__='bmi'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    height = Column(Integer)
    # fix above - figure out how to make it 5'6" format
    weight = Column(Integer)
    bmi = Column(Integer)
    journal_entry = Column(String(500))