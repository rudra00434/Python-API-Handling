POST Request – Send data to a server
import requests
payload = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
print(response.status_code, response.json())
