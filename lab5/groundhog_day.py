def groundhog_day(strings):
    for i in range(1, len(strings)):
        differences = [j for j in range(len(strings[i])) if strings[i][j] != strings[i-1][j]]
        if len(differences) > 2:
            return i, differences
    return 0, 0
