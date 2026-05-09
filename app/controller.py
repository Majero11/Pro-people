# imports methods and objects from flask 
from flask import render_template, request, redirect, url_for, flash, session

from config.database import get_db_connection
from app.models import DatabaseOperations, LeaveOperations, EmployeeOperations, RequestOperations

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
            #create a session 
            session['user_id'] = user[0]
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
    user_id = session['user_id']
    leave_requests =    LeaveOperations.get_leave_requests_by_user_id(user_id)
    user = EmployeeOperations.get_user_details(user_id)

    return render_template('user_dashboard.html', leave_requests=leave_requests, user=user)


@app.route('/submit_leave', methods=['POST'])
def submit_leave():
    """handles the submission of a leave request form
    it gets the user id from the session and the form data for start date, end date and leave type
    it then calls the create_leave_request method from the RequestOperations class to create the leave request in the database
    if the request is created successfully it flashes a success message and redirects the user back to the user dashboard
    if the request creation fails it flashes an error message and redirects the user back to the user dashboard
    """
    user_id = session['user_id']
    
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    leave_type = request.form.get('leave_type')

    success = RequestOperations.create_leave_request(user_id, start_date, end_date, leave_type)
    
    if success:
        flash('Leave request submitted successfully!', 'success')
    else:
        flash('Failed to submit leave request.', 'error')

    return redirect(url_for('user_dashboard'))


@app.route('/admin_dashboard', methods=['GET'])

def admin():
    """render the user_dashboard.html
    """
    return render_template('admin_dashboard.html')
