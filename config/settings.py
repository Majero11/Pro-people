import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config:
    # creat variable in the class that will hold the values from the .env file 
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')
    