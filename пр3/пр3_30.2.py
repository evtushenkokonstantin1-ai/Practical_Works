try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))
    num4 = float(input("Введите четвёртое число: "))

    if num2 == num3 == num4 != num1:
        print("Номер числа: 1")
    elif num1 == num3 == num4 != num2:
        print("Номер числа: 2")
    elif num1 == num2 == num4 != num3:
        print("Номер числа: 3")
    elif num1 == num2 == num3 != num4:
        print("Номер числа: 4")
except ValueError:
    print("Ошибка типа данных")