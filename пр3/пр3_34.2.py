try:
    a = int(input("Введите значение переменной (целое число): "))
    b = int(input("Введите значение переменной (целое число): "))

    if a != b:
        max_n = max(a, b)
        a += max_n
        b += max_n
    elif a == b:
        a, b = 0, 0

    print("Первое число:", a, "\nВторое число:",  b)
except ValueError:
    print("Ошибка типа данных")