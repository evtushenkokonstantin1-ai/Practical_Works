try:
    a = int(input("Введите число А: "))

    print(a < 0)
except ValueError:
    print("Ошибка типа данных")