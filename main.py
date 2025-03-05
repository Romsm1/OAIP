def gauss_elimination(A, b):
    n = len(A)

    # Прямой ход
    for i in range(n):
        # Поиск максимального элемента в столбце (частичный выбор ведущего элемента)
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        # Проверка на вырожденность
        if A[max_row][i] == 0:
            raise ValueError("Система не имеет единственного решения")

        # Перестановка строк
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]

        # Обнуление элементов ниже главной диагонали
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum_ax = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - sum_ax) / A[i][i]

    return x

# Две системы уравнений
systems = [
    {
        "A": [[2, -1, 1], [3, 3, 9], [3, 3, 5]],
        "b": [3, 42, 12],
        "name": "Первая система"
    },
    {
        "A": [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]],
        "b": [1, -2, 0],
        "name": "Вторая система"
    }
]

# Решение и вывод результатов
for system in systems:
    solution = gauss_elimination(system["A"], system["b"])
    print(f"{system['name']}: x ≈ {solution[0]:.2f}, y ≈ {solution[1]:.2f}, z ≈ {solution[2]:.2f}")
