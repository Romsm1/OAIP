def main():
    try:
        # Открываем файл и читаем строки, удаляя лишние пробелы и символы перевода строки
        with open('words.txt', 'r', encoding='UTF8') as file:
            lines = [line.strip() for line in file]

        # Находим длину самого длинного слова
        max_length = 0
        for word in lines:
            if len(word) > max_length:
                max_length = len(word)

        # Собираем все слова с максимальной длиной
        longest_words = []
        for word in lines:
            if len(word) == max_length:
                longest_words.append(word)

        # Выводим результат в зависимости от количества найденных слов
        if len(longest_words) == 1:
            print(f"Слово максимальной длины: {longest_words[0]}")
        else:
            print(f"Слова максимальной длины: {', '.join(longest_words)}")

    except FileNotFoundError:
        print("Файл не найден.")


if __name__ == '__main__':
    main()