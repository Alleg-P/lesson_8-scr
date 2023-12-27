# Задача 3: Минимальная и максимальная цена

assortment = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}

min_product = min(assortment.items(), key=lambda x: x[1])
min_key, min_value = min_product

max_product = max(assortment.items(), key=lambda x: x[1])
max_key, max_value = max_product


print('Самый дешёвый товар:', min_key, min_value, 'руб.')
print('Самый дорогой товар:', max_key, max_value, 'руб.')
