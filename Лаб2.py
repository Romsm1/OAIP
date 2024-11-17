# задание 1
def main():
    str1 = input("Введите строку: ")

    if str1 == "Python":
        print("ДА")
    else:
        print("НЕТ")


# задание 2

    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")

    if (str1 == 'да' or str1 == 'нет') and (str2 == 'да' or str2 == 'нет'):
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")


# задание 3

    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    str3 = input("Введите третью строку: ")

    if (str1 == "раз" and str2 == "два" and str3 == "три") or (str1 == "1" and str2 == "2" and str3 == "3"):
        print("ГОРИ")
    else:
        print("НЕ ГОРИ")


# задание 4

    july_city = input("Введите название города для июля: ")
    august_city = input("Введите название города для августа: ")

    if (july_city == "Тула" and august_city == "Пенза") or (july_city == "Пенза" and august_city == "Тула") or (july_city =="Тула" and august_city == "Тула") or (july_city == "Пенза" and august_city == "Пенза"):
        print("НЕТ")
    else:
        print("ДА")


# задание 5

    n = int(input("Введите кол-во км марафона: "))
    m = int(input("Введите кол-во км которое спортсмен пробегает за день: "))

    if n % m == 0:
        day = n // m
    else:
        day = n // m + 1
    print(f"Спортсмен добежит до финиша на {day} день")


# Задание 6

    digit = input('Введите число: ')

    a = int(digit[0])
    b = int(digit[1])
    c = int(digit[2])

    if (a + c) % 8 != 0 and b == 3:
        print('Подходит')
    else:
        print(a + c, b)

# Задание 7

    category = input('Введите желаемую категорию товара: ')

    if category == "продукты":
        price = int(input("Введите цену товара: "))
        if price < 100:
            print("Попробуйте нашу выпечку!")
        elif 100 <= price < 500:
            print("Как насчёт орехов в шоколаде?")
        else:
            print("Попробуйте экзотические фрукты!")
    else:
        print("Загляните в товары для дома!")

# Задание 8

    a = int(input("Введите цену первого товара: "))
    b = int(input("Введите цену второго товара: "))
    c = int(input("Введите цену третьего товара: "))

    total = a + b + c

    if a < b < c:
        print('Акция!')
        total /= 2
    elif a > b > c:
        print('Акция!')
        total /= 3

    print(f"К оплате: {total} руб.")

# Задание 9

    buyers_vchera = int(input("Введите количество покупателей за вчера: "))
    buyers_pozavchera = int(input("Введите количество покупателей за позавчера: "))

    if buyers_vchera > buyers_pozavchera:
        raznica = buyers_vchera - buyers_pozavchera
        buyers_segodnya = buyers_vchera + raznica
    elif buyers_vchera < buyers_pozavchera:
        raznica = buyers_pozavchera - buyers_vchera
        buyers_segodnya = buyers_vchera - raznica
    else:
        buyers_segodnya = buyers_vchera  

    print(f"Количество покупателей сегодня: {buyers_segodnya}")

# Задание 10

    year = int(input("Введите год: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} является високосным годом.")
    else:
        print(f"{year} не является високосным годом.")

# Задание 11

    number = int(input("Введите число: "))

    if number % 2 == 0:
        print(f"{number} является чётным числом.")
    else:
        print(f"{number} является нечётным числом.")


if __name__ == "__main__":
    main()



