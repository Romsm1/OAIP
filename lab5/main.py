from groundhog_day import groundhog_day
from gears import gears
from brackets import brackets
def main():
    strings = [
        "bnmaa",
        "unxaz",
        "bnmza",
        "bomcv",
        "bnmaz"
    ]
    result1 = groundhog_day(strings)
    print(result1)

    data = [
        [0, 2, 30, 15],
        [14, 3, 21, 60],
        [7, 16, 4, 8]
    ]
    n, m = 30, 7
    result2 = gears(data, n, m)
    print(result2)

    line = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"
    print(brackets(line))
    line = "1{2 + [3}45 - 6] * (7 - 8) 9"
    print(brackets(line))

if __name__ == '__main__':
    main()