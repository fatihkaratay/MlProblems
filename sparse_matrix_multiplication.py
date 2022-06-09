'''
write a function to multiply 2 sparse matrices.
find a way to reduce to computation since sparse matrix mainly consists of 0 (zero)
if  the matrices can't be multiplied together, function should return [[]]

example:
matrix_a = [
    [0, 2, 0],
    [0, -3, 5]
]

matrix_b = [
    [0, 10, 0],
    [0, 0, 0],
    [0, 0, 4]
]

result = [
    [0, 0, 0],
    [0, 0, 20]
]

'''

matrix_a = [
    [0, 2, 0],
    [0, -3, 5]
]

matrix_b = [
    [0, 10, 0],
    [0, 0, 0],
    [0, 0, 4]
]

def sparse_matrix_multiplication(matrix_a, matrix_b):
    return [[]]

print(sparse_matrix_multiplication(matrix_a, matrix_b))