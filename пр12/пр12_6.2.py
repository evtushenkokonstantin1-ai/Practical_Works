#Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.

matrix = [
    [2, 5, 12],
    [4, 15, 7],
    [6, 9, 20]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 10:
            matrix[i][j] = 0

for row in matrix:
    print(row)