try:
    a = int(input("Введите сторону А: "))
    b = int(input("Введите сторону B: "))
    c = int(input("Введите сторону C: "))

    min1 = min(a, b ,c)
    max1 = max(a, b, c)
    print("Наименьшее: ", min1, "\nНаибольшее: ", max1)
except ValueError:
    print("Ошибка типа данных")