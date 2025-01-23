def gears(gears_list, n, m):
    all_gears = [gear for sublist in gears_list for gear in sublist]
    for gear1 in all_gears:
        for gear2 in all_gears:
            if gear1 / gear2 == n / m:
                return gear1, gear2
    return None, None
