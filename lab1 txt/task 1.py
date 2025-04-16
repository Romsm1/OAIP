import random


def random_line():
    with open("lines.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print("Файл пустой.")
        return

    random_line_index = random.choice(lines)
    print(random_line_index)


random_line()
