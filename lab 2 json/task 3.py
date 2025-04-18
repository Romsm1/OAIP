import json

with open('personal_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print("Доступные ключи для изменения:", ", ".join(data.keys()))

key = input('Введите ключ который хотите изменить: ')
value = input(f'Введите новое значение для выбранного ключа "{key}"')

if key in data:
    data[key] = value

    with open('personal_data.json', "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Значение ключа '{key}' успешно изменено на '{value}'.")
else:
    print("Такого ключа нет в данных.")
