# Necessary import
from flask import Flask

# Initialize the flask app
app = Flask('ping')

# Function to check if the service is running
@app.route('/ping', methods = ['GET'])
def ping():
    return "PONG"

# Run the application
if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)