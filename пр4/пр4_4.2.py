try:
    n = int(input("Введите целое число: "))
    num = ""

    while n < 0:
        print("Число должно быль меньше нуля")
        n = int(input("Введите целое число: "))
    while n > 0:
        dig = n % 10
        num += str(dig)
        n = n // 10
    print(num)

except ValueError:
    print("Ошибка типа данных")