try:
    mounth = int(input("Введите номер месяца: "))

    while mounth < 1 or mounth > 12:
        mounth = int(input("Введите номер месяца: "))

    if mounth == 1 or mounth == 2 or mounth == 12:
        print("Зима")
    elif mounth == 3 or mounth == 4 or mounth == 5:
        print("Весна")
    elif mounth == 6 or mounth == 7 or mounth == 8:
        print("Лето")
    elif mounth == 9 or mounth == 10 or mounth == 11:
        print("Осень")
except ValueError:
    print("Ошибка! Неправильный тип данных.")