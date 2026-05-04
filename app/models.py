from config.database import get_db_connection, close_db

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
            query = 'SELECT Employee_id, First_name, Last_name, is_admin from Employees WHERE email = %s AND password = %s'
            
            # execute the query with the provided email and password
            cursor.execute(query, (email, password))
            
            user = cursor.fetchone()
            cursor.close()
            close_db()
            return user
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
        finally:
            close_db()