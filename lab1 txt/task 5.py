try:
    with open('input.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    chars = len(content)

    bits = chars * 8
    bytes = bits / 8

    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    size = bytes
    unit_index = 0

    while size >= 1024 and unit_index < len(units) -1:
        size /= 1024
        unit_index += 1

    print(f"Размер текста: {size:.2f} {units[unit_index]}")

except FileNotFoundError:
    print("Файл не найден!")
