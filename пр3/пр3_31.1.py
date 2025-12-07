try:
    a = int(input("Введите сторону А: "))
    b = int(input("Введите сторону B: "))
    c = int(input("Введите сторону C: "))

    while a >= b + c or b >= a + c or c >= a + b:
        print("Треугольник не существует! \nВведите длину сторон заново: ")
        a = int(input("Введите сторону А: "))
        b = int(input("Введите сторону B: "))
        c = int(input("Введите сторону C: "))

    print(a == b != c or a != b == c or a == c != b)
except ValueError:
    print("Ошибка типа данных")