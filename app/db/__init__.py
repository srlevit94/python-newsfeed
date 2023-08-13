from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g 

load_dotenv()

# connect to database using env variable
# manages overall connection to db
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# generates temporary connections for performing CRUS operartions
Session = sessionmaker(bind=engine)
# maps models to real MySQL tables
Base = declarative_base()

#tells Flask to run whenever a context is destroyed
def init_db(app):
  Base.metadata.create_all(engine)
  app.teardown_appcontext(close_db)

#whenever function is called, returns a new session
def get_db():
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()
  return g.db

def close_db(e=None):
  # attempts to find and remove db from g object
  db = g.pop('db', None)
# if db exists, close it
  if db is not None:
    db.close()