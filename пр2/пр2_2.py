weight_x = int(input("Введите вес шоколадных конфет: "))
price_x = int(input("Введите цену шоколадных конфет: "))
weight_y = int(input("Введите вес ирисок: "))
price_y = int(input("Введите цену ирисок: "))

price_chocolate = price_x / weight_x
price_toffee = price_y / weight_y

diff = price_x / price_y

print(f"Дороже в {diff} раз(а)")