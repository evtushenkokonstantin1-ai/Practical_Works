try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))

    max1 = max(num1, num2, num3)
    min_n = min(num1, num2, num3)
    max2 = num1 + num2 + num3 - max1 - min_n
    summa = max1 + max2
    print(summa)
except ValueError:
    print("Ошибка типа данных")