import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///../fitness_app.db')

engine = create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(bind=engine))
