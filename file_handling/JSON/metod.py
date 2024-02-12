'''
          JSON  Методтору!

json.dump()
json.dumps()
json.load()
json.loads()

'''

import json

# Пример данных в формате словаря Python
daany = {
    "имя": "John",
    "возраст": 30,
    "город": "New York",
    "хобби": ["плавание", "музыка", "путешествия"]
}

# Кодирование (сериализация) данных в формат JSON
json_s = json.dumps(daany)

print("JSON-строка:", json_s)

b = json.loads(json_s)

print(f"Восстановленные данные: {b}", )
