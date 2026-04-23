# import the psycopg package 
import psycopg

# import thr class config that contains the database connevtion parameters 
from config.settings import config 

class Database:
    """we are goto use the singleton pattern to manage the PostgreSQL connection.
    
    Attributes:
        _instance: singleton instance of the class  
    """
    
    _instance = None 
    
    def __init__(self):
        try:
            self._instance = psycopg.connect(
                host=config.DB_HOST,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                dbname=config.DB_NAME,
                port=config.DB_PORT 
            )
            
            # display a message to indicate that the connection was successful
            print("Database connection established successfully.")
        except psycopg.OperationalError as e:
            print(f"Error connecting to the database: {e}")
            
    @classmethod
    def get_instance(cls):
        """Private method to get the singleton instanve of the class.
        
        Returns:
            database connection instance
        """
        if cls._instance in None:
            cls._instance = cls()
        return cls._instance
    
    def _close_connection(self):
        """Private method to close the database connection."""
        if self._instance is not None:
            self._instance.close()
            print("Database connection closed.")

def get_db_connection():
    """Public method to get the database connection instance.
    
    Returns:
        database connection instance
    """
    return Database.get_instance()

def close_db_connection():
    """Public method to close the database connection."""
    Database._close_connection()
    Database._instance = None