7# задание 1
def main():
    number = " "
    for _ in range(8):
        a = input()
        number += a
    print(number)

# задание 2
    names = int(input("введите кол-во имен: "))
    for i in range(1, names + 1):
        name = input("введите имя: ")
        print(f"{i},{name}")

# задание 3
    n = int(input("введите начальную дату: "))
    m = int(input("введите шаг цикла: "))
    for day in range(n, 32, m):
        print(day," ",end="")

# задание 4
    target = input("буква для которой нужно найти повторения:")
    letters = int(input("введите кол-во букв: "))
    max_count = 0 # макс кол-во подряд
    current_count = 0 # кол-во идущих подряд

    for _ in range(letters):
        letter = input("вводите по одной букве: ")
        if letter == target:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    print(f"Максимум идущих подряд: {max_count}")

# задание 5
    number = int(input("Введите число: "))
    a = 0 # делители
    for i in range(1, number + 1):
        if number % i == 0:
            a += i
    print(f"Сумма делителей = {a}")

# задание 6
    vowels = "аяоёэеуюыи"
    count = 0
    line = input("Введите строку: ").split()

    for word in line:
        vowel_count = 0
        for char in word:
            if char in vowels:
                vowel_count += 1
        if vowel_count > 0:
            count += vowel_count - 1

    print(count)


# Задание 7
    word = input("Слово: ")
    n = int(input("Натуральное число n: "))
    for i in range(1, n + 1):
        print(word)

# Задание 8
    number = input("Введите номер телефона:")
    for num in number:
        if num not in "0123456789+":
            print("Неправильный номер телефона!")
            break
    else:
        print("Правильный номер телефона")

# Задание 9
    password = input("Введите пароль: ")
    bukvi = "ЙйЦцКкНнГгШшЩщЗзХхЪъФфВвПпРрЛлДдЖжЭэЧчСсМмТтЬьБб"
    secret_pass = ""

    for letter in password:
        if letter in bukvi:
            secret_pass += '1'
        else:
            secret_pass += '0'

    print(secret_pass)

# Задание 10
    a = 'ППррииввеетт!!  ККаакк  ддееллаа??  ССееггоодднняя  ттааккааяя  ххоорроошшааяя  ппооггооддаа,,  ммоожжеетт  ппооггуулляяеемм??'
    correct = ''.join(a[i] for i in range(len(a)) if i == 0 or a[i] != a[i - 1])
    print(correct)

if __name__ == '__main__':
    main()
