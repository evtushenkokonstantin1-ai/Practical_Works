try:
    a = int(input("Введите сторону А: "))
    b = int(input("Введите сторону B: "))
    c = int(input("Введите сторону C: "))

    hyp = max(a, b, c)
    if hyp == a:
        cat1 = b
        cat2 = c
    elif hyp == b:
        cat1 = a
        cat2 = c
    elif hyp == c:
        cat1 = b
        cat2 = a
    print(hyp**2 == cat1**2 + cat2**2)
except ValueError:
    print("Ошибка типа данных")