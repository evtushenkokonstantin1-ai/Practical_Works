A = int(input("Введите положительное число A: "))
B = int(input("Введите положительное число B: "))
C = int(input("Введите положительное число C: "))

rec = A * B
square = C * 4
count = rec // square
empty = rec % square

print("Количество квадратов: ", count, "\nНезанятая область: ", empty)