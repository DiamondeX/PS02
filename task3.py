import requests

# Словарь с данными для отправки
new_post = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# URL для API JSONPlaceholder для создания новых постов
url = "https://jsonplaceholder.typicode.com/posts"

# Отправка POST-запроса
response = requests.post(url, json=new_post)

# Распечатка статуса ответа
print("Status Code:", response.status_code)

# Распечатка содержимого ответа
if response.status_code == 201 or response.status_code == 200:  # 201 - Created, 200 - OK
    print("Response Content:")
    print(response.json())
else:
    print("No content returned or error occurred")