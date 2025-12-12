try:
    P = float(input("Введите процент: "))
    sl = 10
    K = 0
    S = 0

    while 0 < P < 0.5 and sl < 200:
        S += sl
        sl += sl * P
        K += 1
    print(f"Количество дней: {K}, Суммарный пробег: {S}")
except ValueError:
    print("Ошибка типа данных")