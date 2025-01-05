# Necessary import
import requests

# Image url
url = 'http://localhost:8080/predict'

# Input data
data = {'url': 'http://bit.ly/mlbookcamp-pants'}

# Sending request
result = requests.post(url, json = data).json()
# Get response
print(result)