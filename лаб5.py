# Задание 1
def main():
    n = int(input("Введите количество чисел: "))
    digits = set()

    for _ in range(n):
        number = input("Введите число: ")
        digits.update(number) # update добавляет уникальные числа из введеных чисел в множество

    print("Количество различных использованных цифр:", len(digits))

# задание 2
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")
    string3 = input("Введите третью строку: ")

    set1 = set(string1)
    set2 = set(string2)
    set3 = set(string3)

    letters = (set1 & set2) | (set1 & set3) | (set2 & set3)

    result = ''.join(letters)
    print(result)

# задание 3
    digit = input("Введите число: ")
    all_digits = set('0123456789')

    true_digits = set(digit)
    missing_digits = all_digits - true_digits

    result = ' '.join(missing_digits)
    print(result)


if __name__ == '__main__':
    main()
