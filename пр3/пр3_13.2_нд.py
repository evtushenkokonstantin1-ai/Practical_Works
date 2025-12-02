year = int(input("Введите год: "))

if year in range(0, 2025, 4):
    print("Год", year, "- високосный")
else:
    print("Год", year, "- обычный")