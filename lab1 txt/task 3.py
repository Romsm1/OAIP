with open('lines.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    even_lines = [line.strip() for i, line in enumerate(lines) if i % 2 == 1]
    odd_lines = [line.strip() for i, line in enumerate(lines) if i % 2 == 0]

    for line in even_lines:
        print(f"Четная строка: {line}")
    for line in odd_lines:
        print(f"Нечетная строка: {line}")
