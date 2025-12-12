try:
    price = float(input("Введите цену за 1 кг: "))
    weight = 1
    pr = price

    while price <= 0:
        print("Цена не может быть меньше или равной нулю")
        price = float(input("Введите цену за 1 кг: "))

    while weight <= 2:
        print(pr)
        weight += 0.2
        pr = price * weight
except ValueError:
    print("Ошибка типа данных")