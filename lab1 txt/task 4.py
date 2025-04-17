try:
    with open('words.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]

    max_length = 0
    for word in lines:
        if len(word) > max_length:
            max_length = len(word)

    longest_words = []
    for word in lines:
        if len(word) == max_length:
            longest_words.append(word)

    if len(longest_words) == 1:
        print(f"Слово максимальной длины: {longest_words[0]}")
    else:
        print(f"Слова максимальной длины: {', '.join(longest_words)}")

except FileNotFoundError:
    print("Файл не найден.")

