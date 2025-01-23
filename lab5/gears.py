def gears(data, n, m):
    for box in data:
        for gear1 in box:
            for box2 in data:
                for gear2 in box2:
                    if gear1 / gear2 == n / m:
                        return (gear1, gear2)
    return (None, None)

