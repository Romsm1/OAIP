# Вводите два числа через пробел, например: 200 60
print("Введите n (мин. сумма баллов) и m (мин. балл по каждому предмету):")
n, m = map(int, input().split())

# Теперь вводите строки с данными абитуриентов
print("Теперь вводите данные абитуриентов, например: Иванов Петр 70 80 90")

with open('exam.csv', 'w', encoding='utf-8') as out_file:
    out_file.write('Фамилия;имя;результат 1;результат 2;результат 3;сумма\n')

    while True:
        try:
            line = input()
            data = line.split()

            surname, name = data[0], data[1]
            scores = list(map(int, data[2:]))
            total = sum(scores)

            if total >= n and all(s >= m for s in scores):
                result_line = f'{surname};{name};{scores[0]};{scores[1]};{scores[2]};{total}\n'
                out_file.write(result_line)
        except:
            break