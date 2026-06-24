#В матрице элементы первого столбца возвести в куб.

matrix = [
    [2, 5, 12],
    [4, 15, 7],
    [6, 9, 20]
]

for i in range(len(matrix)):
    matrix[i][0] = matrix[i][0] ** 3

for row in matrix:
    print(row)