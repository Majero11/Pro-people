# imports methods and objects from flask 
from flask import render_template, request, redirect, url_for, flash

from config.database import get_db_connection

from app import app

# create a route for the home page
@app.route('/', methods=['GET'])
def index():
    """render the index.html
    """
    return render_template('index.html')


@app.route('/user_dashboard', methods=['GET'])
def user_dashboard():
    """render the user_dashboard.html
    """
    return render_template('user_dashboard.html')