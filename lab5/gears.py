def gears(gear_lists, n, m):
    # Перебираем все шестерёнки из каждого списка
    for i in range(len(gear_lists)):
        for j in range(len(gear_lists[i])):
            for k in range(i, len(gear_lists)):
                for l in range(len(gear_lists[k])):
                    # Пропускаем одинаковые шестерёнки из одного списка
                    if i == k and j == l:
                        continue
                    # Проверяем условие на передаточное число
                    if gear_lists[i][j] * m == gear_lists[k][l] * n:
                        return (gear_lists[i][j], gear_lists[k][l])
    return (None, None)  # Если ничего не найдено
