#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
matrixA = [
        [1, 2, 4],
        [3, 5, 7]
        ]
matrixB = [[7, 9, 12], [4.5, 12, 8]]
print(matrix_divided(matrix, 3))
print(matrix)
try:
    print(matrix_divided("School", 3))
except Exception as err:
    print(err)
try:
    print(matrix_divided(matrixA, "Tsh"))
except Exception as err:
    print(err)
try:
    print(matrix_divided())
except Exception as err:
    print(err)
