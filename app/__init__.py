# import necessary modules and functions 
from flask import Flask 
from config.settings import Config
from config.database import close_db_connection

# initialize the Flask class 
# __name__ helps flask locat the resources of the application 
app = Flask(__name__)

# use the secret key from the config file to secure the session data 
app.secret_key = Config.SECRET_KEY

# load configurations from the config file 
app.config.from_object(Config)

# close the database automatically after each request 
@app.teardown_appcontext
def teardown_db(exception):
    """Function to close the database connection after each request."""
    close_db_connection()
    
# ensure the object app is fully initialixed before importin the routes
from app import app

