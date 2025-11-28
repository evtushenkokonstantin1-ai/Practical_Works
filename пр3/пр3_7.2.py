unit_w = int(input("Введите число 1-5: "))
weight = float(input("Введите массу тела: "))

if unit_w == 1:
    b_weight = weight
    print(b_weight, "Килограмм")
elif unit_w == 2:
    b_weight = weight / 1000000
    print(b_weight, "Килограмм")
elif unit_w == 3:
    b_weight = weight / 1000
    print(b_weight, "Килограмм")
elif unit_w == 4:
    b_weight = weight * 1000
    print(b_weight, "Килограмм")
elif unit_w == 5:
    b_weight = weight * 100
    print(b_weight, "Килограмм")