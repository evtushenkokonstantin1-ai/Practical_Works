try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    count = 0
    nums = a

    while nums <= b:
        print(nums)
        nums += 1
        count += 1
    print("Количество: ", count)
except ValueError:
    print("Ошибка типа данных")