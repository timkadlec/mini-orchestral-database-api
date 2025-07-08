import requests

url = "http://127.0.0.1:5000/api/instruments"
data = {
    "name": "Trumpet",
    "abbreviation": "Tpt"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
