try:
    a = int(input("Введите число A: "))
    b = int(input("Введите число B: "))
    c = int(input("Введите число C: "))
    print(a < b + c and b < a + c and c < a + b)
except ValueError:
    print("Ошибка типа данных")