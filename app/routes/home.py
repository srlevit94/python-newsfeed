#import Blueprint() and render_template() from the Flask module
from flask import Blueprint, render_template, session, redirect
from app.models import Post
from app.db import get_db

#lets us consolidate routes into a single bp object that parent can access later
bp = Blueprint('home', __name__, url_prefix='/')

#turns index and login into routes
#render template makes function respond with a template instead of string
@bp.route('/')
def index():
  # get all posts
  db = get_db()
  posts = db.query(Post).order_by(Post.created_at.desc()).all()
  return render_template(
    'homepage.html',
    posts=posts,
    loggedIn=session.get('loggedIn')
  )

@bp.route('/login')
def login():
  # not logged in yet
  if session.get('loggedIn') is None:
    return render_template('login.html')
  return redirect('/dashboard')

# <id> is a parameter
@bp.route('/post/<id>')
def single(id):
  # get single post by id
  db = get_db()
  #specify the SQL WHERE clause
  post = db.query(Post).filter(Post.id == id).one()
  # render single post template
  return render_template(
    'single-post.html',
    post=post,
    loggedIn=session.get('loggedIn')
  )