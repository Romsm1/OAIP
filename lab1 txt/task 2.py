try:
    with open('prices.txt', 'r', encoding='utf-8') as file:
        total_cost = 0.0

        for line in file:
            parts = line.strip().split('\t')  # Разделяем строку по табуляции
            if len(parts) == 3:
                name, quantity, price = parts
                try:
                    quantity = int(quantity)
                    price = float(price)
                    total_cost += quantity * price
                    line_processed = True
                except ValueError:
                    continue

        if total_cost > 0:
            print(f"{total_cost:.2f}")
        else:
            print("Файл пустой.")

except FileNotFoundError:
    print("Файл prices.txt не найден.")
