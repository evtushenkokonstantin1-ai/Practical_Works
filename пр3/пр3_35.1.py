try:
    num = int(input("Введите число: "))

    if num > 0:
        num += 1
    elif num < 0:
        num -= 2
    else:
        num = 0

    print(num)
except ValueError:
    print("Ошибка типа данных")