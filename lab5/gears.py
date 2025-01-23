def gears(data, n, m):
    for i, box1 in enumerate(data):
        for gear1 in box1:
            for j, box2 in enumerate(data):
                if i != j:  # Проверяем, чтобы шестерёнки были из разных коробок
                    for gear2 in box2:
                        if gear1 / gear2 == n / m:
                            return (gear1, gear2)
    return (None, None)