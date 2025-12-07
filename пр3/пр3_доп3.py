try:
    num = int(input("Введите двузначное число: "))

    f_dig = num // 10
    s_dig = num % 10

    while num < 10 or num > 99 or num == 0:
        print("Ошибка! Число не может лежать вне диапазона 10-99 или равняться нулю")
        num = int(input("Введите двузначное число: "))

    if (f_dig + s_dig) % 2 == 0:
        num += 2
    else:
        num -= 2

    print(num)
except ValueError:
    print("Ошибка типа данных")