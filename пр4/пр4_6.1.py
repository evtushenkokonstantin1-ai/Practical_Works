try:
    a = int(input("Введите число A: "))
    b = int(input("Введите число B: "))
    s = 0

    while a > b:
        print("Число А должно быть меньше B!")
        a = int(input("Введите число A: "))
        b = int(input("Введите число B: "))

    while a <= b:
        s += a
        a += 1
    print(s)
except ValueError:
    print("Ошибка типа данных")