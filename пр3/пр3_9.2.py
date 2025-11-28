N = int(input("Введите номер мат. действия 1-4: "))
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if N == 1:
    r = a + b
    print(r)
elif N == 2:
    r = a - b
    print(r)
elif N == 3:
    r = a * b
    print(r)
elif N == 4:
    r = a / b
    print(r)