a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

if a != b:
    s = a + b
    a = s
    b = s
    print("Первое число: ", a, "\nВторое число: ", b)
elif a == b:
    a = 0
    b = 0
    print("Первое число: ", a, "\nВторое число: ", b)