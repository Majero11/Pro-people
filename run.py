# entry point to the application 
from app import app

if __name__ == '__main__':
    # run the application in debug mode 
    app.run(host="0.0.0.0", port=8080, debug=True)
    
    