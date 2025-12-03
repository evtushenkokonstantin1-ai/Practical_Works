try:
    x = int(input("Введите координату X: "))
    y = int(input("Введите координату Y: "))
    print((x < 0 < y) or (x < 0 and y < 0 ))
except ValueError:
    print("Ошибка типа данных")