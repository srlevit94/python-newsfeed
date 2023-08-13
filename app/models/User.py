from app.db import Base
# define columns and data types
from sqlalchemy import Column, Integer, String
# validates data before it is stored in the database
from sqlalchemy.orm import validates

import bcrypt
#create salt to hash passwords against
salt = bcrypt.gensalt()

# User class includes id, username, email, and password
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)
  
  #validates email address
  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email
    return email
  
  @validates('password')
  def validate_password(self, key, password):
    # makes sure password is at least 4 characters long
    assert len(password) > 4
    #encrypt password
    return bcrypt.hashpw(password.encode('utf-8'), salt)