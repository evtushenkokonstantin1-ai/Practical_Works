try:
    conf = int(input("Введите сумму вклада: "))

    while conf < 1:
        print("Число не может быть меньше 1")
        conf = int(input("Введите сумму вклада: "))

    if conf <= 50000:
        print(4, "%", sep="")
    elif 50000 < conf <= 100000:
        print(5, "%", sep="")
    elif 100000 < conf <= 150000:
        print(6, "%", sep="")
    elif 150000 < conf <= 200000:
        print(7, "%", sep="")
except ValueError:
    print("Ошибка типа данных")