# import the psycopg package 
import psycopg

# import the class config that contains the database connection parameters 
from config.settings import Config 

class Database:
    """ 
    use the singleton  pattern manage the PostgreSQL connection 
    
    Attributes:
        _instance: songleton of the class 
    """
    
    _instance = None
    
    def __init__(self):
        try:
            self.conn = psycopg.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            
        except psycopg.OperationalError as e:
            print(f"Error connection to the database: {e}")
            
    @classmethod
    def get_instance(cls):
        """
        Private method to get the singleton instance of the class 
        Returns: 
            the database connection instance
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    @classmethod
    def close_db_connection(cls):
        """
        Method to close the database connection 
        """
        if cls._instance is not None:
            cls._instance.conn.close()
            
def get_db_connection():
    """
    Public method to get the database connection instance 
    Returns:
        the database connection instance
    """
    return Database.get_instance().conn

def close_db():
    """
    Public method to close the database connection 
    """
    Database.get_instance().close_db_connection()
    Database._instance = None