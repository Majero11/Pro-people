# imports methods and objects from flask 
from flask import render_template, request, redirect, url_for, flash, session

from config.database import get_db_connection

from app import app

# create a route for the home page 
@app.route('/', methods=['GET', 'POST'])
def index():
    """render the index page """
    return render_template('index.html')