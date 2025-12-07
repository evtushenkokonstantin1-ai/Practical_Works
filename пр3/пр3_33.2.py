try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))

    min_1 = min(num1, num2, num3)

    print("Минимальное: ", min_1)
except ValueError:
    print("Ошибка типа данных")