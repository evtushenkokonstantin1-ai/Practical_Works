try:
    a = int(input("Введите число A: "))
    b = int(input("Введите число B: "))
    prod = a

    while a > b :
        print("Первое число должно быль меньше второго!")
        a = int(input("Введите число A: "))
        b = int(input("Введите число B: "))

    while a < b:
        a += 1
        prod *= a
    print(f"Произведение: {prod}")
except ValueError:
    print("Ошибка типа данных")