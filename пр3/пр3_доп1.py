try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    prod = num1 * num2

    while num1 == 0 or num2 == 0:
        print("Число не может равняться нулю")
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

    if prod < 0:
        prod *= 8
    else:
        prod *= 1.5

    print(prod)
except ValueError:
    print("Ошибка типа данных")