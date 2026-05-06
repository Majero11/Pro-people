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
            query = 'SELECT user_id, first_name, last_name, is_admin from users WHERE email = %s AND password = %s'
            
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
            
            query = 'SELECT request_id, start_date, days_applied, status FROM leave_requests WHERE user_id = %s'
            cursor.execute(query, (user_id,))            
            return cursor.fetchall()

        
        except Exception as e:
            print(f"Error fetching leave requests: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            close_db_connection()