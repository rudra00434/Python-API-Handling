PUT Request – Update existing data
payload = {"id": 1, "title": "updated"}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=payload)
print(response.json())
