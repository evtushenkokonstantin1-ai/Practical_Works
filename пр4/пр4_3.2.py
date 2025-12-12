try:
    n = int(input("Введите целое число: "))

    while n < 0:
        print("Число должно быль меньше нуля")
        n = int(input("Введите целое число: "))

    while n > 0:
        dig = n % 10
        if dig == 2:
            print("True")
            break
        n = n // 10
    else:
        print("False")
except ValueError:
    print("Ошибка типа данных")