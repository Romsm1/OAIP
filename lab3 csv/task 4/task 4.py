# Чтение и обработка данных
with open('file.csv', encoding='utf-8') as f:
    items = [line.strip().split(';') for line in f]
    items = [[name, int(price)] for name, price in items]

money = 1000
basket = []
items.sort(key=lambda x: x[1])  # Сортировка по цене

# Основная логика покупок
for name, price in items:
    count = min(10, money // price)
    if count > 0:
        basket += [name] * count
        money -= price * count

# Вывод результатов
if basket:
    print("Покупки:", ", ".join(f"{name}×{basket.count(name)}" for name in sorted(set(basket))))
    print("Осталось:", money)
else:
    print("Ничего не куплено")