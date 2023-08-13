#import Blueprint() and render_template() from the Flask module
from flask import Blueprint, render_template

#lets us consolidate routes into a single bp object that parent can access later
bp = Blueprint('home', __name__, url_prefix='/')

#turns index and login into routes
#render template makes function respond with a template instead of string
@bp.route('/')
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

# <id> is a parameter
@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')