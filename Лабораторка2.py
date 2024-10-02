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

buyers_pozavchera = int(input("Введите количество покупателей за позавчера: "))
buyers_vchera = int(input("Введите количество покупателей за вчера: "))

if buyers_vchera > buyers_pozavchera:
    raznica = buyers_vchera - buyers_pozavchera
    buyers_segodnya = buyers_vchera + raznica
else:
    raznica = buyers_pozavchera - buyers_vchera
    buyers_segodnya = buyers_vchera - raznica

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
