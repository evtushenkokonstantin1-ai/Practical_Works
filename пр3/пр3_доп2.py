try:
    num = int(input("Введите число: "))

    while num == 0:
        print("Число не может равняться нулю")
        num = int(input("Введите число: "))

    if num % 2 == 0:
        num /= 4
    elif num % 2 == 1:
        num *= 5

    print(num)
except ValueError:
    print("Ошибка типа данных")