from pprint import pprint

import requests

# URL для API GitHub поиска репозиториев
url = "https://api.github.com/search/repositories"

# Параметры запроса
params = {
    'q': 'language:html'  # Ищем репозитории с языком HTML
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Печать статуса ответа
print("Status Code:", response.status_code)

# Проверка, что ответ успешен
if response.status_code == 200:
    # Печать содержимого ответа в формате JSON
    data = response.json()
    print("Response Content:")
    pprint(data)
else:
    print("There was an error with status code:", response.status_code)