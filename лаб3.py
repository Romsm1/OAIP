# задание 1
def main():
    abc = input("Введите строку: ")
    while abc != " ":
        print(f"Длина строки: {len(abc)}")
        abc = input("Введите строку: ")

    # задание 2

    negative_numbers = 0
    while (number := float(input())) < 36.6:
        if number < 0:
            negative_numbers += 1
    print(negative_numbers)

    # задание 3

    num1_max = num2_max = float(input("Введите число: "))
    while (number := float(input("Введите число: "))) < 1000:
        if number > num1_max:
            num2_max = num1_max
            num1_max = number
        elif number > num2_max and number != num1_max:
            num2_max = number

    print(f"Второй максимум = {num2_max}"
          
    # задание 4
    numbers = input("Введите числа через пробел: ").split()  # split нужен для того чтобы считать строку и разбить ее на отдельные элементы
    min_number = float(numbers[0])
    i = 1

    while i < len(numbers):
        if float(numbers[i]) < min_number:
            min_number = float(numbers[i])
        i += 1

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
    a = 1

    while a <= 10000:
            celoe_number = True
            if a < 2:
                celoe_number = False
            else:
                i = 2
                while i <= int(a**0.5):
                    if a % i == 0:
                        celoe_number = False
                        break
                    i += 1
            if celoe_number:
            summa += a
            a += 1

    print(f"Сумма простых чисел: {summa}")

# задание 7
    x = int(input("Ширина большой коробки: "))
    y = int(input("Длина большой коробки: "))
    z = int(input("Высота большой коробки: "))

    b_box = x * y * z
    s_boxes = 0
    n = int(input("Введите количество маленьких коробок: "))
    i = 0  # отслеживание кол-ва введенных коробок

    while i < n:
        a = int(input("Ширина маленькой коробки: "))
        b = int(input("Длина маленькой коробки: "))
        c = int(input("Высота маленькой коробки: "))

        s_box = a * b * c
        s_boxes += s_box
        i += 1

    if s_boxes <= b_box:
        print("Да")
    else:
        print("Нет")


# задание 8
    min_word = input("Введите первое слово: ")
    word = input("Введите следующее слово (или 'стоп' для завершения): ")

    while word != "стоп":
        if len(word) < len(min_word):  
            min_word = word  
        word = input("Введите следующее слово (или 'стоп' для завершения): ")

    print(f"Самое короткое слово: {min_word}")


# задание 9
    result = float(input("Введите число: "))
    operation = input("Введите операцию (+, -, *, /) или 'стоп' для завершения: ")

    while operation != "стоп":
        next_number = float(input("Введите следующее число: "))
        if operation == "+":
            result += next_number
        elif operation == "-":
            result -= next_number
        elif operation == "*":
            result *= next_number
        elif operation == "/":
            result /= next_number  

        operation = input("Введите операцию (+, -, *, /) или 'стоп' для завершения: ")

    print("Результат работы: ", result)

# задание 10
    sentence = ""  
    word = input()  
    while word != "стоп":  
        if sentence:  
            sentence += " "
        sentence += word  
        word = input() 
    if sentence:  
        print(sentence)

    

if __name__ == "__main__":
    main()
