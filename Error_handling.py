try:
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()  # Raises HTTPError if status is 4xx or 5xx
    data = response.json()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("General Error:", err)
