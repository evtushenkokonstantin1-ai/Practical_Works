a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))

mid = a + b + c - min(a, b, c) - max(a, b, c)

print("Среднее: ", mid)