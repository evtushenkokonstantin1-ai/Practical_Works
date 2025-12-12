try:
    n = int(input("Введите целое число: "))
    s = 0
    count = 0
    while n < 0:
        print("Число должно быль меньше нуля")
        n = int(input("Введите целое число: "))

    while n > 0 :
        s += n % 10
        n //= 10
        count += 1
    print(f"Сумма: {s}, Количество: {count}")
except ValueError:
    print("Ошибка типа данных")