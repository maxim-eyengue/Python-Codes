####### Subscription Prediction with downloaded models #######

# necessary import
import pickle

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

# New customer information
customer = {
    "job": "management",
    "duration": 400,
    "poutcome": "success"
}

# One-Hot-Encoding
X = dv.transform([customer])
# Make soft predictions
y_pred = model.predict_proba(X)[0, 1]

# Print result
print("Subscription_probability", y_pred)