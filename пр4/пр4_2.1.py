try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    nums = b
    count = 0

    while a < b and nums > a + 1:
        nums -= 1
        count += 1
        print(nums)
    print("Количество: ", count)
except ValueError:
    print("Ошибка типа данных")