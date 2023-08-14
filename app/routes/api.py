from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db
import sys 

bp = Blueprint('api', __name__, url_prefix='/api')

# route to create a new user after signing up
@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()
  print(data)

  try:
    newUser = User(
      username = data['username'],
      email = data['email'],
      password = data['password']
    )
    # save in database
    # prep the INSERT statement and the db.commit() method
    db.add(newUser)
    db.commit()
  except:
    print(sys.exe_info()[0])
    # insert failed, so rollback and send error to front end
    db.rollback()
    return jsonify(message = 'Signup failed'), 500
  
  # clears any existing session data and creates two new session properties:
  # a user_id to aid future database queries and a Boolean property that the templates will use to conditionally render elements.
  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True

  return jsonify(id = newUser.id)
  
#clears login session
@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204
  
@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()

  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])
    
    return jsonify(message = 'Incorrect credentials'), 400

  if user.verify_password(data['password']) == False:
    return jsonify(message = 'Incorrect credentials'), 400

  # creates session and sends back valid response
  session.clear()
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)

# {'username': 'shanetestfinal', 'email': 'final@email.com', 'password': 'final123'}