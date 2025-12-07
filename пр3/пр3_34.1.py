try:
    num = int(input("Введите число: "))

    if num > 0:
        num += 1
        print(num)
    else:
        print(num)
except ValueError:
    print("Ошибка типа данных")