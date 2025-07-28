DELETE Request – Delete a resource
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # Should be 200 or 204
