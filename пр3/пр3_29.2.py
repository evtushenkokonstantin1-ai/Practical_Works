try:
    a = float(input("Введите число А: "))
    b = float(input("Введите число B: "))
    c = float(input("Введите число C: "))

    if abs(a - b) < abs(a - c):
        print("Точка: B", "\nРасстояние: ", b)
    elif abs(a - b) > abs(a - c):
        print("Точка: C", "\nРасстояние: ", c)
    else:
        print("Числа равны")
except ValueError:
    print("Ошибка типа данных")