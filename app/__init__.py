# import the necessary modules and functions
from flask import Flask 
from config.settings import Config
from config.database import close_db_connection

# initialize an instance of the Flask class 
# __name__ helps flask locate the resources of the application 
app = Flask(__name__)

# use the secret key from the config class to secure the data 
app.config['SECRET_KEY'] = Config.SECRET_KEY

# load configurations from the config file 
app.config.from_object(Config)

# close the database automatically after each request 
@app.teardown_appcontext
def teardown_db(exception):
    """fucntion to close the database connection after each request.
    """
    close_db_connection()
    
# Ensure the object app is fully initialized before importing the routes 
from app import controller