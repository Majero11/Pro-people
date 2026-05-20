from config.database import get_db_connection, close_db_connection
from psycopg.rows import dict_row
# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import validates

# db = SQLAlchemy()

class DatabaseOperations:
    @staticmethod
    def get_user(email, password):
        try:
            # connect to the database
            conn = get_db_connection()
            
            # create a cursor 
            cursor = conn.cursor()
            
            if cursor is None:
                return None
            
            # write the query to fetch the user with the given email and password
            query = 'SELECT user_id, first_name, last_name, is_admin from users  WHERE email = %s AND password = %s'
            
            # execute the query with the provided email and password
            cursor.execute(query, (email, password))
            
            user = cursor.fetchone()
            cursor.close()
            return user
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
        finally:
            close_db_connection()
            
class LeaveOperations:
    
    @staticmethod
    def get_leave_requests_by_user_id(user_id):
        conn = None
        cursor = None
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor(row_factory=dict_row)
            
            if cursor is None:
                return None
            
            query = 'SELECT request_id, start_date, end_date, days_applied, status FROM leave_requests WHERE user_id = %s'
            cursor.execute(query, (user_id,))            
            return cursor.fetchall()

        
        except Exception as e:
            print(f"Error fetching leave requests: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            close_db_connection()


class EmployeeOperations:
    
    @staticmethod
    def get_user_details(user_id):
        conn = None
        cursor = None
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor(row_factory=dict_row)
            
            if cursor is None:
                return None
            
            query = 'SELECT user_id, first_name, last_name, position, email, contact, department_name FROM users u JOIN departments d ON u.department_id = d.department_id WHERE u.user_id = %s'
            cursor.execute(query, (user_id,))            
            return cursor.fetchone()

        
        except Exception as e:
            print(f"Error fetching leave requests: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            close_db_connection()
            
class RequestOperations:
    
    @staticmethod
    def create_leave_request(user_id, start_date, end_date, leave_type):
        conn = None
        cursor = None
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            if cursor is None:
                return False
            
            query = 'INSERT INTO leave_requests (user_id, start_date, end_date, leave_type) VALUES (%s, %s, %s, %s)'
            cursor.execute(query, (user_id, start_date, end_date, leave_type))
            conn.commit()
            return True

        
        except Exception as e:
            print(f"Error creating leave request: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            close_db_connection()
            
    @staticmethod
    def delete_leave_request(request_id, user_id):
        conn = None
        cursor = None
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            if cursor is None:
                return False
            
            query = 'DELETE FROM leave_requests WHERE request_id = %s AND user_id = %s'
            cursor.execute(query, (request_id, user_id))
            conn.commit()
            return True

        
        except Exception as e:
            print(f"Error deleting leave request: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            close_db_connection()
            
    @staticmethod
    def update_user_details(user_id, password, email, contact):
        conn = None
        cursor = None
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            if cursor is None:
                return False
            
            if password and password.strip():
                query = 'UPDATE users SET password = %s, email = %s, contact = %s WHERE user_id = %s'
                
                cursor.execute(query, (password, email, contact, user_id))
            else:
              query = 'UPDATE users SET email = %s, contact = %s WHERE user_id = %s'
            
            cursor.execute(query, (email, contact, user_id))
            conn.commit()
            return True

        
        except Exception as e:
            print(f"Error updating user details: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            close_db_connection()
            
class AdminOperations:
    @staticmethod
    def get_all_user_requests():
        conn = None
        cursor = None
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor(row_factory=dict_row)
            
            if cursor is None:
                return None
            
            query = 'SELECT lr.request_id, u.first_name, u.last_name, lr.leave_type, lr.start_date, lr.end_date, lr.days_applied, lr.status FROM leave_requests lr JOIN users u ON lr.user_id = u.user_id ORDER BY lr.request_id DESC'
            cursor.execute(query)            
            return cursor.fetchall()

        
        except Exception as e:
            print(f"Error fetching leave requests: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            close_db_connection()
            
    @staticmethod
    def get_admin_requests():
        conn = None
        cursor = None
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor(row_factory=dict_row)
            
            if cursor is None:
                return None
            
            query = 'SELECT lr.request_id, u.first_name, u.last_name, lr.leave_type, lr.start_date, lr.end_date, lr.days_applied, lr.status FROM leave_requests lr JOIN users u ON lr.user_id = u.user_id WHERE u.is_admin = TRUE ORDER BY lr.request_id DESC'
            cursor.execute(query)            
            return cursor.fetchall()

        
        except Exception as e:
            print(f"Error fetching leave requests: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            close_db_connection()
            
    @staticmethod
    def get_all_users():
        conn = None
        cursor = None
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor(row_factory=dict_row)
            
            if cursor is None:
                return None
            
            query = "SELECT u.user_id, CONCAT(u.first_name, ' ', u.last_name) AS name, u.position, d.department_name, u.email, u.contact FROM users u LEFT JOIN departments d ON u.department_id = d.department_id ORDER BY u.user_id DESC"
            cursor.execute(query)            
            return cursor.fetchall()

        
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            close_db_connection()
            
    @staticmethod
    def update_leave_request(request_id, status):
        conn = get_db_connection()
        cursor = conn.cursor(row_factory=dict_row)
        
        try:
            query = ' UPDATE leave_requests SET status = %s, approved_at = current_timestamp WHERE request_id = %s'
            
            values = (status, request_id)
            cursor.execute(query, values)
            conn.commit()
            
            return True
            
        except Exception as e:
            print(f"Error updating status: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def delete_user(user_id):
        conn = None
        cursor = None
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = 'DELETE FROM users WHERE user_id = %s'
            cursor.execute(query, (user_id,))
            conn.commit()
            return True

        
        except Exception as e:
            print(f"Error user: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            close_db_connection()

    @staticmethod
    def create_user(first_name, last_name, email, password, department_id, is_admin, contact, position):
        conn = None
        cursor = None
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = 'INSERT INTO users (first_name, last_name, email, password, department_id, is_admin, contact, position) VALUES (%s, %s, %s, %s,%s,%s,%s,%s)'
            cursor.execute(query, (first_name, last_name, email, password, department_id, is_admin, contact, position))
            conn.commit()
            return True
        
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            close_db_connection()
            


# class Departments(db.Model):
#     __tablename__ = "departments"
#     department_id = db.Column(db.Integer, primary_key=True)
#     department_name = db.Column(db.String(50), nullable=False)

# class Users(db.Model):
#     __tablename__ = "users"
#     user_id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(20), nullable=False)
#     last_name = db.Column(db.String(25), nullable=False)
#     email = db.Column(db.String(25), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)
#     department_id = db.Column(
#         db.Integer,
#         db.ForeignKey("departments.department_id")
#     )
#     created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
#     is_admin = db.Column(db.Boolean, nullable=False, default=False)
#     contact = db.Column(db.String(13))
#     position = db.Column(db.String(30))

# class LeaveRequest(db.Model):
#     __tablename__ = "leave_requests"
#     request_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
#     leave_type = db.Column(db.String(50), nullable=False)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date, nullable=False)
#     status = db.Column(db.String(20), nullable=False, default="pending")
#     requested_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
#     approved_by = db.Column(db.Integer, nullable=True)
#     approved_at = db.Column(db.DateTime(timezone=True), nullable=True)
#     days_applied = db.Column(db.Integer, nullable=False)
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         if self.start_date and self.end_date:
#             self.days_applied = (self.end_date - self.start_date).days + 1