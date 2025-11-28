K = int(input("Введите номер дня: "))

first_day = 6
offset = ((first_day  - 1) + (K - 1)) % 7 + 1

print("Номер дня: ", offset)