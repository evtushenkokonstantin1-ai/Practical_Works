try:
    x = int(input("Введите координату X: "))
    y = int(input("Введите координату Y: "))
    print(y < 0 < x)
except ValueError:
    print("Ошибка типа данных")