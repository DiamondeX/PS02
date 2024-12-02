import requests

# URL для API JSONPlaceholder c фильтрацией по userId
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса
params = {
    'userId': 1  # Фильтруем посты по userId равному 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверка статуса ответа
if response.status_code == 200:
    # Получение данных в формате JSON
    posts = response.json()

    # Печать полученных записей
    for post in posts:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("---")
else:
    print("Request failed with status code:", response.status_code)