try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    summa = num1 + num2

    while summa == 0:
        print("Число не может равняться нулю!")
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

    if summa % 5 == 0:
        summa += 1
    else:
        summa -= 2

    print(summa)
except ValueError:
    print("Ошибка типа данных")