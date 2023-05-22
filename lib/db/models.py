from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from enum import Enum as PyEnum
import uuid
import click

Base = declarative_base()
id = Column(Integer, primary_key=True)
name = Column(String(50))
new_column = Column(String(100))  # New column definition

class ExerciseType(PyEnum):
    CARDIO = 1
    STRENGTH_TRAINING = 2
    FLEXIBILITY = 3
    STRENGTH = 4

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_info'
    username = Column(String, primary_key=True)
    password = Column(String)

    #food_logs = relationship("FoodLog", back_populates="user")  # Define the relationship with the FoodLog model


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

    #user_username = Column(String, ForeignKey('users.username'))
    #user = relationship("User", back_populates="fitness_logs")

class FoodLog(Base):
    __tablename__ = 'food_logs'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    food = Column(String)
    calories = Column(Integer)
    journal_entry = Column(String)
    #user_username = Column(String, ForeignKey('users.username'))  # Define the foreign key relationship

    #user = relationship("User", back_populates="food_logs")  # Define the relationship with the User model

class BMI(Base):
    __tablename__ = 'bmi'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    height = Column(Integer)
    weight = Column(Integer)
    bmi = Column(Integer)
    journal_entry = Column(String(500))

    #user_username = Column(String, ForeignKey('users.username'))
    #user = relationship("User", back_populates="bmis")


def init_db(engine):
    Base.metadata.drop_all(bind=engine, tables=[User.__table__])
