unit_l = int(input("Введите единицу длины: "))
length = float(input("Введите длину отрезка: "))

if unit_l == 1:
    b_length = length / 10
    print(b_length, "Метров")
elif unit_l == 2:
    b_length = length * 1000
    print(b_length, "Метров")
elif unit_l == 3:
    b_length = length
    print(b_length, "Метров")
elif unit_l == 4:
    b_length = length / 1000
    print(b_length, "Метров")
elif unit_l == 5:
    b_length = length / 100
    print(b_length, "Метров")
