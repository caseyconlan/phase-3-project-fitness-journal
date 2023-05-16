from sqlalchemy import Column, Integer, String, Date, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum

Base = declarative_base()

class ExerciseType(PyEnum):
    CARDIO = "cardio"
    STRENGTH = "strength"

class MuscleGroup(PyEnum):
    ARMS = "arms"
    CORE = "core"
    LEGS = "legs"
    OTHER = "other"

class FitnessLog(Base):
    __tablename__ = 'fitness_logs'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    exercise = Column(String)
    exercise_type = Column(Enum(ExerciseType))
    weight_or_speed = Column(Integer)
    reps_or_time = Column(Integer)
    muscle_group = Column(Enum(MuscleGroup))
    journal_entry = Column(Text)

    def __repr__(self):
        return f"<FitnessLog(id={self.id}, date={self.date}, exercise={self.exercise}, exercise_type={self.exercise_type}, weight_or_speed={self.weight_or_speed}, reps_or_time={self.reps_or_time}, muscle_group={self.muscle_group}, journal_entry={self.journal_entry})>"
