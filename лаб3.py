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

    numbers = input("Введите числа через пробел: ").split() # .split нужен для того чтобы считать строку и разбить ее на отдельные элементы
    min_number = float(numbers[0])

    for number in numbers:
        if float(number) < min_number:
            min_number = float(number)
    print(f"Наименьшее число = {min_number}")



# задание 5

    





if __name__ == "__main__":
    main()
