def gears(gear_list, n, m):
    for i in range(len(gear_list)):
        for j in range(i + 1, len(gear_list)):
            if gear_list[i] * m == gear_list[j] * n:
                return (gear_list[i], gear_list[j])
    return (None, None)