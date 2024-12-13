# import for making requests
import requests

# request url
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

# image data info
data = {'url': 'http://bit.ly/mlbookcamp-pants'}

# Get a response from our request
result = requests.post(url, json = data).json()
# Print the result
print(result)