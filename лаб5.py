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

    # задание 4
    numbers = []
    num = " "
    while num != 0:
        num = int(input("Введите число (0 для завершения ввода): "))
        if num != 0:
            numbers.append(num)

    length = len(numbers)
    result = []

    for num in numbers:
        if num % length == 0:
            result.append(num)

    print(f"Числа, кратные длине последовательности:, {result}")
    

    # задание 5
    num_colors = int(input("Введите количество цветов для флагов: "))
    colors = []

    for _ in range(num_colors):
        color = input("Введите цвет флага: ")
        colors.append(color)

    num_flags = int(input("Введите количество флагов в гирлянде: "))
    garland = []
    for i in range(num_flags):
        garland.append(colors[i % num_colors])  

    print(f"Цвета флагов идущих в гирлянде: {garland}")
    print(" ".join(garland))

    # задание 6
        age = input("Введите возраст находок: ")

    while age != '':
        age = int(age)
        if age >= 4500:
            print(f"{age} тысяч лет - Archaea")
        elif 2500 <= age < 4500:
            print(f"{age} тысяч лет - Proterozoic")
        elif 541 <= age < 2500:
            print(f"{age} тысяч лет - Paleozoic")
        elif 252 <= age < 541:
            print(f"{age} тысяч лет - Mesozoic")
        elif age < 252:
            print(f"{age} тысяч лет - Cenozoic")
        age = input("Введите возраст находок (Enter для завершения): ")

    # задание 7
    bird_counts = {}

    while (line := input()) != '':
        bird, count = line.split(': ')
        count = int(count)
        if bird in bird_counts:
            bird_counts[bird] += count
        else:
            bird_counts[bird] = count

    print(bird_counts)

    # задание 8
    numbers = input().split()

    result = [
        {
            'digits': len(binary_representation := bin(int(number))[2:]),
            'units': binary_representation.count('1'),
            'zeros': binary_representation.count('0')
        }
        for number in numbers
    ]

    print(result)



if __name__ == '__main__':
    main()
