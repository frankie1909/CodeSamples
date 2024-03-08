import requests
import json

base_url = 'https://hp-api.onrender.com/api'
endpoint = '/characters'
headers = {'Accept': 'application/json'}

response = requests.get(url=f"{base_url}{endpoint}", headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"Name: {data['name']}")
    print(f"wand {data['wood']}")
    print(
        f"Year of birth: {requests.get(data['yearOfBirth'],headers=headers).json()['name']}")
else:
    print(response.status_code)
