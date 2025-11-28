weight_x = int(input("Введите вес: "))
price_x = int(input("Введите цену: "))
weight_y = int(input("Введите вес: "))

price = price_x / weight_x
price_y = (weight_y + 1) * price

print("Цена конфет: ", price_y)