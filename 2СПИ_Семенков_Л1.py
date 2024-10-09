# задание 1

def main():

    movie = input("Название фильма: ")
    cinema = input("Название кинотеатра: ")
    time = input("Время: ")

    print(f'Билет на "{movie}" в "{cinema}" на {time} забронирован.')

if __name__ == "__main__":
    main()


# задание 2

def main():

    paycheck = float(input("Зарпалата за месяц: "))
    w_hours = float(input("Кол-во раб часов в выходные: "))

    premiya = paycheck * 0.01 * w_hours

    print(f"Размер премии: {premiya}")

if __name__ == "__main__":
    main()


# задание 3

def main():
    summa = int(input("Введите сумму: "))

    number_1000 = summa // 1000
    rem_amount = summa % 1000

    number_100 = rem_amount // 100
    rem_amount %= 100

    number_10 =rem_amount // 10
    number_1 = rem_amount % 10

    print(f"{number_1} по 1р")
    print(f"{number_10} по 10р")
    print(f"{number_100} по 100р")
    print(f"{number_1000} по 1000р")

if __name__ == "__main__":
    main()


# задание 4

def main():
    review = input("Напишите отзыв: ")
    review = review.lower()

    a = review.find("весело")
    b = review.find("увлекательно")
    c = review.find("развлечения")

    print(f"Результат анализа: {a} {b} {c}")

if __name__ == "__main__":
    main()


# заdание 5

def main():
    a = input()
    length = len(a)

    if length % 2 !=0:
        mid_index = length // 2
        print(a(mid_index))
    else:
        mid_index = length // 2 - 1
        print(a[mid_index])

if __name__ == "__main__":
    main()


# задание 6

def main():
    feedback = 'Алиса и Вася, большое спасибо за теплый приём!'
    name1 = feedback[0:5]
    name2 = feedback[8:12]

    result = name1 + "/" + name2
    print(f"Назначить премию: {result}")

if __name__ == "__main__":
    main()

# задание 7

def main():
    alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    a = int(input("Введите номер буквы: "))
    index = a - 1
    for i in range(4):
        print(alfavit[(index + i) % 26], end=' ')

if __name__ == "__main__":
    main()


# задание 8

new_list = []  # Создание пустого списка
new_list = [1, 2, 3, 4, 5]  # Присвоение списка чисел

new_list.append(6)  # Добавление элемента в конец списка
new_list.extend([7, 8])  # Добавление нескольких элементов из другого списка

new_list.remove(2)  # Удаление первого найденного элемента 2 из списка
del new_list[0]  # Удаление элемента по индексу 0

s_list = new_list[2:5]  # Срез списка с элементами от 2 до 4 индекса (5 не включается)

new_list.reverse()  # Изменение порядка элементов на обратный
reversed_list = new_list[::-1]  # Создание нового списка с элементами в обратном порядке

list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Создание двумерного списка (списка списков)

element = list_2d[1][2]  # Доступ к элементу 2-й строки и 3-го столбца (значение 6)
list_2d[0][1] = 10  # Замена значения в первом подсписке на индексе 1

new_list.clear()  # Очистка списка


#задание 9

empty_tuple = ()  # Создание пустого кортежа
print(empty_tuple)  # Вывод пустого кортежа

fulled_tuple = (1, 2, 3, "ошцоуопшцпоупбцущп", 6323.3277779876767)  # Создание кортежа с различными элементами
print(fulled_tuple)  # Вывод кортежа

# задание 10

empty_set = set()
print(empty_set)

fulled_set = {1, 2, 3, "klwofojf", 802.214}
print(fulled_set)

empty_set.add(4)
empty_set.add(5)
empty_set.add("ABC")
print(empty_set)

# объединение
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print(union_set)
# пересечение
intersection_set = set_a.intersection(set_b)
print(intersection_set)
# разность
difference_set = set_a.difference(set_b)
print(difference_set)
# cимметричная разность
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)

# задание 11

empty_dict = {}
print(empty_dict)

fulled_dict = {
    "name": "Roman",
    "age": 18,
    "city": "Blagoveshchensk"
}
print(fulled_dict)

fulled_dict["job"] = "Student"
print(fulled_dict)

del fulled_dict["name"]
print(fulled_dict)

fulled_dict["age"] = "3286"
print(fulled_dict)
