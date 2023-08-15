from flask import session, redirect
# functools is a module for higher order functions
from functools import wraps

#receives another function as an argument
def login_required(func):
  @wraps(func)
  def wrapped_function(*args, **kwargs):
    #if logged in, call orginal function with origiginal arguments
    if session.get('loggedIn') == True:
      return func(*args, **kwargs)
    return redirect('/login')
  
  return wrapped_function