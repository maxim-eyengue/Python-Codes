# Necessary import
import requests

# Set the correct external-IP address
External_IP_address = "None"

# Image url 
url = f'http://{External_IP_address}/predict'

# Input data
data = {'url': 'http://bit.ly/mlbookcamp-pants'}

# Sending request
result = requests.post(url, json = data).json()
# Get response
print(result)