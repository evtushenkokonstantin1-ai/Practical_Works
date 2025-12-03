year = int(input("Введите год: "))

if year % 4 == 0 and year != 300 and year != 1300 and year != 1900:
    print("Год", year, "- високосный")
else:
    print("Год", year, "- обычный")