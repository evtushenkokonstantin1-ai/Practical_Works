a = float(input("Введите число A: "))
b = float(input("Введите число B: "))
c = float(input("Введите число C: "))

if a < b < c:
    a = a * 2
    b = b * 2
    c = c * 2
    print(a, b, c)
else:
    a = -a
    b = -b
    c = -c
    print(a, b, c)
