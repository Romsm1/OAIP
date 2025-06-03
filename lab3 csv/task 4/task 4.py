import csv

with open('file.csv', encoding='utf-8') as f:
    items = [[row[0], int(row[1])] for row in csv.reader(f, delimiter=';')]

money = 1000
basket = []
items.sort(key=lambda x: x[1])  # Сортируем от дешёвых к дорогим

for name, price in items:
    # Максимум 10 каждого товара
    can_buy = min(10 - basket.count(name), money // price)
    if can_buy > 0:
        basket += [name] * can_buy
        money -= price * can_buy

    # Покупаем другие товары, если остались деньги
    for other_name, other_price in items:
        if other_name != name and other_price <= money:
            basket.append(other_name)
            money -= other_price

print(', '.join(basket) if basket else 'error')
print(f"Остаток: {money} руб.")