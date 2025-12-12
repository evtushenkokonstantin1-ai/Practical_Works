try:
    price = float(input("Введите цену за 1 кг: "))
    weight = 0.1
    pr = price

    while price <= 0:
        print("Цена не может быть меньше или равной нулю")
        price = float(input("Введите цену за 1 кг: "))

    while weight <= 1:
        weight += 0.1
        pr = price * weight
        print(pr)
except ValueError:
    print("Ошибка типа данных")