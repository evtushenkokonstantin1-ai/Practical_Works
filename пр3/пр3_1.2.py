try:
    x = int(input("Введите x координату  точки: "))
    y = int(input("Введите y координату  точки: "))

    if x and y > 0:
        print("1 четверть")
    elif x < 0 and y > 0:
        print("2 четверть")
    elif x < 0 and y < 0:
        print("3 четверть")
    elif x > 0 and y < 0:
        print("4 четверть")
except ValueError:
    print("Ошибка типа данных")