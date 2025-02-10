import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# print(response.json()['title'])

# url = 'https://jsonplaceholder.typicode.com/posts'

# data = {'title': 'foo', 'body': "bar", "userId": 1}

# response = requests.post(url, json = data)
# print(response.status_code)
# print(response.json())


# url = 'https://jsonplaceholder.typicode.com/posts/1'
# # data = {'title': 'updated title', 'body': "new body", "userId": 1}

# # response = requests.put(url, json = data)
# # print(response.status_code)
# # print(response.json())

# response = requests.delete(url)
# print(response.status_code)

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 59.9343,
    "longitude": 30.3353,
    'current_weather': True
    }

response = requests.get(url, params = params)

if response.status_code == 200:
    data = response.json()
    print(data['current_weather']['temperature'])
else:
    print("Ошибка при запросе:", response.status_code)


"""
Напишите класс Character обладающий 3 характеристиками: атака, здоровье, уклонение
FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

Класс имеет следующие методы:
Распределение атрибутов как описано выше: character_1 = Character("fighter")
Атака
Получение урона в случае если увернуться не удалось.
Уклонение: каждое очко уклонения умножается на 5. Результат уклонения зависит от рандомно генерируемого числа
от 0 до 100. Если это число меньше или равно навыка уклонения, то герой уклоняется от атаки.
Смерть: если здоровье меньше 1.

Напишите функцию которая заставит сразиться разных героев друг с другом 100 раз. Выведите счет.
"""