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
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    sparse_a = get_dict_of_nonzero_cells(matrix_a)
    sparse_b = get_dict_of_nonzero_cells(matrix_b)

    res_matrix = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    for i, k in sparse_a.keys():
        for j in range(len(matrix_b[0])):
            if (k, j) in sparse_b.keys():
                res_matrix[i][j] += sparse_a[(i, k)] * sparse_b[(k, j)]
    return res_matrix


def get_dict_of_nonzero_cells(matrix):
    dict_of_nonzero_cells = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                dict_of_nonzero_cells[(i, j)] = matrix[i][j]
    return dict_of_nonzero_cells


print(sparse_matrix_multiplication(matrix_a, matrix_b))
