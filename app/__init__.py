# imports flask function
from flask import Flask

# imports home and dashboard modules
from app.routes import home, dashboard, api
# imoirts init_db function
from app.db import init_db
from app.utils import filters

# def keyword defines create_app function
def create_app(test_config=None):
    # set up app config
    # app serves static resources from root directory
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    # should use a key when creating server site settings
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )
    
    # inner function called hello()
    #@app.route('/hello')
    #def hello():
        #return 'hello world'
    
    # register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(api)

    init_db(app)

    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural

    return app
