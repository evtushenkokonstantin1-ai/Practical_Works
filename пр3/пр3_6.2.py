n = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))
op = input("Введите операцию - + / *: ")

if op == "+":
    print(n + n2)
elif op == "-":
    print(n - n2)
elif op == "*":
    print(n * n2)
elif op == "/":
    print(n / n2)