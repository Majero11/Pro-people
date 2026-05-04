# imports methods and objects from flask 
from email.mime import message
from flask import render_template, request, redirect, url_for, flash, session

from app.models import DatabaseOperations
from config.database import get_db_connection

from app import app

# create a route for the home page
@app.route('/', methods=['GET', "POST"])
def index():
    """handles user login process
    for Get request it renders the login page 
    For POST it attempts to log the user in by checking the email and password against the database
     If the login is successful it redirects the user to the user dashboard
     If the login fails it flashes an error message and redirects back to the login page
    """
    if request.method == 'POST':
        # get the form data
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = DatabaseOperations.get_user(email, password)
        
        if user is not None:
            # create a session for the user
            session['employee_id'] = user[0]
            session['first_name'] = user[1]
            session['last_name'] = user[2]
            session['is_admin'] = user[3]
            
            if session['is_admin']:
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
            

        flash('Wrong credentials. Please try again.', 'error')
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/user_dashboard', methods=['GET'])
def user_dashboard():
    """render the user_dashboard.html
    """
    return render_template('user_dashboard.html')