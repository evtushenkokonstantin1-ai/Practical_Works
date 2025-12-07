try:
    a = int(input("Введите число A: "))
    b = int(input("Введите число B: "))

    print(a % 2 == 0 or b % 2 == 0)
except ValueError:
    print("Ошибка типа данных")