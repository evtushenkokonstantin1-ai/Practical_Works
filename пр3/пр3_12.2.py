num = int(input("Введите число: "))

if num == 0:
    print("Нулевое число")
elif num < 0 and num % 2 == 0:
    print("Отрицательное чётное число")
elif num > 0 and num % 2 == 0:
    print("Положительное чётное число")
elif num < 0 and num % 2 == 1:
    print("Отрицательное нечётное число")
elif num > 0 and num % 2 == 1:
    print("Положительное нечётное число")