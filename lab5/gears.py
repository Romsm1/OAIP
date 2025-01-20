def gears(data, n, m):
    for gear_list1 in data:
        for gear_list2 in data:
            for gear1 in gear_list1:
                for gear2 in gear_list2:
                    if gear1 * m == gear2 * n:
                        return gear1, gear2
    return None, None