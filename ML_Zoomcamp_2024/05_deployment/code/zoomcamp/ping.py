####### Web Service #######
# Necessary import
from flask import Flask

# Create the app
app = Flask("ping")

# decorator to link the function to our app
@app.route("/ping", methods = ['GET'])
def ping():
    # return result
    return "PONG"

# Condition to execute code only if run as a script
if __name__ == "__main__":
    # Run application in debug mode, specifying the localhost
    app.run(debug = True, host = '0.0.0.0', port = 9696)
