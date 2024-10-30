### Subscription & Marketing Services Interaction ###

# import necessary library
import requests

# url address for making predictions
url = "http://localhost:9696/q4_predict"

# New customer information
customer = {
    "job": "student",
    "duration": 280,
    "poutcome": "failure"
    }

# send a request for making predictions
response = requests.post(url, json = customer).json()
# Print the response
print(response)

# Send a promotional email if necessary
if not response['Subscription']:
    print('sending promotional email to', 'MJ-35')
else:
    print('not sending promotion to', 'MJ-35')