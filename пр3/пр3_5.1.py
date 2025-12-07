try:
    a = int(input("Введите число A: "))
    b = int(input("Введите число B: "))
    print(a > 0 and b < -2)
except ValueError:
    print("Ошибка типа данных")