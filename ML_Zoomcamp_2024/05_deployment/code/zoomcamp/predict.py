####### Churn Web Service #######

# necessary import
import pickle
from flask import Flask, request, jsonify

# Name of the model
model_file = 'model_C=1.0.bin'

# Open model file to read it
with open(model_file, 'rb') as f_in:
    # Load the model
    dv, model = pickle.load(f_in)

# Create the app
app = Flask("churn")

# decorator to link the function to our app
@app.route("/predict", methods = ['POST']) # `POST` method as we send some information about the customer
def predict():
    # Get the .json data
    customer = request.get_json()
    
    # One-Hot-Encoding
    X = dv.transform([customer])
    # Make soft predictions
    y_pred = model.predict_proba(X)[0, 1]
    # Make decision
    churn = y_pred >= 0.5
    
    # Prepare response
    result = {
        "churn_probability": float(y_pred),
        "churn": bool(churn)
    }
    # return the result
    return jsonify(result)
    

# Condition to execute code only if run as a script
if __name__ == "__main__":
    # Run application in debug mode and specifying the localhost
    app.run(debug = True, host = '0.0.0.0', port = 9696)