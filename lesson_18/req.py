import requests

url = 'http://127.0.0.1:8000/advice'

data = {'text':"Смейтесь чаще, собаки!"}
response = requests.post(url, json=data)

print(response.json())