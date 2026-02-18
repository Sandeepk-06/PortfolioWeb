import requests

url = "http://127.0.0.1:5000/chat"
payload = {"message": "Hello, who are you?"}
try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except Exception as e:
    print("Request failed:", e)
