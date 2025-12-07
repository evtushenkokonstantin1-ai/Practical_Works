try:
    a = int(input("Введите число А: "))

    print(a % 2 == 0)
except ValueError:
    print("Ошибка типа данных")