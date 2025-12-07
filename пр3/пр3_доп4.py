try:
    num = int(input("Введите число: "))

    while num == 0:
        print("Число не может равняться нулю!")
        num = int(input("Введите число: "))

    if num > 0:
        num += 20
    else:
        num -= 5

    print(num)
except ValueError:
    print("Ошибка типа данных")