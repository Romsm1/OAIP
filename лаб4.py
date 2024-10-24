# задание 1
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
    line = input("введите строку: ").split()
    vowel = "аяоёэеуюыи" # гласные
    count = 0
    for word in line:
        for letter in word:
            if letter in vowel:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
