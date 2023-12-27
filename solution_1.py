# Задача 1: Словарь цен

assortment = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
product = input("Введите товар: ")

if product in assortment:
    print("Цена: ", assortment[product])
else:
    print("Товар отсутствует.")
