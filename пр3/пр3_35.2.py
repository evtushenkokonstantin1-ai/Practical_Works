try:
    a = int(input("Введите сторону А: "))
    b = int(input("Введите сторону B: "))
    c = int(input("Введите сторону C: "))
    count_pos = 0
    count_neg = 0

    if a > 0:
        count_pos += 1
    elif a < 0:
        count_neg += 1
    if b > 0:
        count_pos += 1
    elif b < 0:
        count_neg += 1
    if c > 0:
        count_pos += 1
    elif c < 0:
        count_neg += 1

    print("Количество положительных:", count_pos, "Количество отрицательных: ", count_neg)
except ValueError:
    print("Ошибка типа данных")