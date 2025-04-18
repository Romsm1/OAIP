import json

# Открываем JSON-файл
file_name = "personal_data.json"
with open(file_name, "r", encoding="utf-8") as file:
    data = json.load(file)

# Выводим ключи для выбора
print("Доступные ключи:", ", ".join(data.keys()))

# Запрашиваем ключ и новое значение
key = input("Введите ключ для изменения: ")
new_value = input(f"Введите новое значение для '{key}': ")

# Изменяем значение в словаре
if key in data:
    data[key] = new_value
    # Перезаписываем файл
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Значение ключа '{key}' успешно изменено на '{new_value}'.")
else:
    print("Такого ключа нет в данных.")