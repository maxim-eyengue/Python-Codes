### Churn & Marketing Services Interaction ###

# Necessary library
import requests

# url address for making predictions
url = "http://localhost:9696/predict"

# New customer information
customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 24,
    "monthlycharges": 29.85,
    "totalcharges": 24 * 29.85
}

# Send a request for making predictions
response = requests.post(url, json = customer).json()
# Print the response
print(response)

# Send a promotional email if necessary
if response['churn']:
    print('sending email to', 'MJ-35')
else:
    print('not sending promotion to', 'MJ-35')
