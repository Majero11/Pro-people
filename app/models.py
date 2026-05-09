from config.database import get_db_connection, close_db_connection
from psycopg.rows import dict_row


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
            
            #write the query to fetch the user with the given email and password
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