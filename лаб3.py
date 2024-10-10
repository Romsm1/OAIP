# задание 1
def main():
    while True:
        abc = input("Введите строку: ")
        if abc == " ":
            break
        print(f"Длина строки: {len(abc)}")

    # задание 2

    negative_numbers = 0

    while True:
        number = float(input("Введите число: "))
        if number > 36.6:
            break
        if number < 0:
            negative_numbers += 1

        print(negative_numbers)

    # задание 3

    num1_max = num2_max = float(input("Введите число: "))
    while True:
        number = float(input("Введите число: "))
        if number >= 1000:
            break
        if number > num1_max:
            num2_max = num1_max
            num1_max = number
        elif number > num2_max and number != num1_max:
            num2_max = number

        print(f"Второй максимум = {num2_max}")

    # задание 4

    numbers = input(
        "Введите числа через пробел: ").split()  # .split нужен для того чтобы считать строку и разбить ее на отдельные элементы
    min_number = float(numbers[0])

    for number in numbers:
        if float(number) < min_number:
            min_number = float(number)
    print(f"Наименьшее число = {min_number}")


# задание 5

    number = int(input("Введите число: "))

    while number != 0:
        if number == 0:
            break
        if number % 3 == 0 and number % 7 == 0:
            print("Караул!")
            break
        elif number % 3 == 0:
            print("Несчастливое")
        elif number % 7 == 0:
            print("Опасное")
        else:
            print(number)
        number = int(input("Введите число: "))


# задание 6

    summa = 0
    for a in range(1, 10001):
        celoe_number = True
        if a < 2:
            celoe_number = False
        else:
            for i in range(2, int(a**0.5) + 1):
                if a % i == 0:
                    celoe_number = False
                    break
        if celoe_number:
            summa += a
    print(f"Cумма простых числе: {summa}")

# задание 7

if __name__ == "__main__":
    main()
