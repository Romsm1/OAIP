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

    if (july_city == "Тула" and august_city == "Пенза"):
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


if __name__ == "__main__":
    main()


