####### Serving the Subscription Web Service #######

# necessary import
import pickle
from flask import Flask, request, jsonify

# Model and vectorizer filenames 
model_file, dv_file = 'model1.bin', 'dv.bin'

# Function to load files
def load_file(file_name):
    # Open the file to read it
    with open(file_name, 'rb') as f_in:
        # return the file content
        return pickle.load(f_in)

# Load model and vectorizer
model, dv = load_file(model_file), load_file(dv_file)

# Create the app
app = Flask("subscription")

# decorator to link the function to our app
@app.route("/q4_predict", methods = ['POST']) # `POST` method as we send some information about the customer
def predict():
    # Get the .json data
    customer = request.get_json()
    
    # One-Hot-Encoding
    X = dv.transform([customer])
    # Make soft predictions
    y_pred = model.predict_proba(X)[0, 1]
    # Make decision
    subscription = y_pred >= 0.5
    
    # Prepare response
    result = {
        "Subscription_probability": float(y_pred),
        "Subscription": bool(subscription)
    }
    # return the result
    return jsonify(result)
    

# Condition to execute code only if run as a script
if __name__ == "__main__":
    # Run application in debug mode and specifying the localhost
    app.run(debug = True, host = '0.0.0.0', port = 9696)