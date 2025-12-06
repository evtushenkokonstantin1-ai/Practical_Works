try:
    a = float(input("Введите сторону А: "))
    b = float(input("Введите сторону B: "))
    c = float(input("Введите сторону C: "))

    print(a == b == c)
except ValueError:
    print("Ошибка типа данных")