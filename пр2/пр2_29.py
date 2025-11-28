K = int(input("Введите номер дня недели от 1-365: "))

first_day = 1
offset = first_day + (K - 1) % 7

print("Номер дня недели: ", offset)