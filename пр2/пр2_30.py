K = int(input("Введите номер дня 1-365: "))

first_day = 4
offset = ((first_day - 1) + (K - 1)) % 7 + 1

print("Номер дня недели: ", offset)