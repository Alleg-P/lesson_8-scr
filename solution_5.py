# Задача 5: Уникальные товары для двух магазинов

products_1 = input('Первый магазин: ')
shop_1 = set(products_1.split(", "))
products_2 = input('Второй магазин: ')
shop_2 = set(products_2.split(", "))

exclusiv_shop_1 = shop_1.difference(shop_2)
exclusiv_shop_2 = shop_2.difference(shop_1)

print('Только в первом магазине:', ", ".join(exclusiv_shop_1))
print('Только в втором магазине:', ", ".join(exclusiv_shop_2))
