import json

data = {
    "first_name": "Sanek",
    "last_name": "Prigoda",
    "surname": "Dmitrivich",
    "year_birth": 2005,
    "city_birth": "Poyarkovo",
    "place_study": "BGPU"
}

with open('personal_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    print("JSON-файл успешно создан!")
