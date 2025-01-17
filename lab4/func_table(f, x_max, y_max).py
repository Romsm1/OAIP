def func_table(f, x_max, y_max):
    for y in range(y_max + 1):
        row = []
        for x in range(x_max + 1):
            row.append(str(eval(f)))
        print('\t'.join(row))
