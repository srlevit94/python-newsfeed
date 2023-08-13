# imports flask function
from flask import Flask

# imports home and dashboard modules
from app.routes import home, dashboard

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

    return app
