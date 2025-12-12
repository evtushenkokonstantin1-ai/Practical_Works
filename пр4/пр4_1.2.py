try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    rec = a * b
    sq = c * c
    s = sq
    count = 0

    while s <= rec:
        count += 1
        s += sq
    print(count)
except ValueError:
    print("Ошибка типа данных")