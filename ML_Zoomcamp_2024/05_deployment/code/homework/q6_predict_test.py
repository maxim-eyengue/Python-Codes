### Subscription & Marketing Services Interaction ###

# import necessary library
import requests

# url address for making predictions
url = "http://localhost:9696/q6_predict"

# New customer information
customer = {
    "job": "management",
    "duration": 400,
    "poutcome": "success"
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