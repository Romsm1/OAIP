def groundhog_day(strings):
    for i in range(1, len(strings)):
        difference = [diff for diff in range(len(strings[i])) if strings[i][diff] != strings[i - 1][diff]]
        if len(difference) > 2:
            return 1, difference
        return 0, 0