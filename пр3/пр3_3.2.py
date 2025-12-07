try:
    price = float(input("Введите цену: "))

    while price <= 0:
        print("Число не может быть меньше 1")
        price = float(input("Введите цену: "))

    if price <= 500:
        print(2, "%", sep="")
    elif 500 < price <= 1000:
        print(3, "%", sep="")
    elif 1000 < price <= 1500:
        print(4, "%", sep="")
    elif 1500 < price <= 2000:
        print(5, "%", sep="")
except ValueError:
    print("Ошибка типа данных")