print('sparse_matrix representation')

# Python program for Sparse Matrix Representation
# using arrays

# assume a sparse matrix of order 4*5
# let assume another matrix compactMatrix
# now store the value,row,column of arr1 in sparse matrix compactMatrix

sparseMatrix = [[0, 0, 3, 0, 4], [0, 0, 5, 7, 0], [0, 0, 0, 0, 0], [0, 2, 6, 0, 0]]

# initialize the size as 0
size = 0

for i in range(4):
    for j in range(5):
        if sparseMatrix[i][j] != 0:
            size += 1
print('compact matrix size is ', size)

'''
number of columns in the compact matrix should be equal to size of non zero
elements in the sparse matrix
'''

rows, cols = (3, size)

compact_matrix = [[0 for i in range(cols)] for j in range(rows)]

k = 0
for i in range(4):
    for j in range(5):
        if sparseMatrix[i][j] != 0:
            compact_matrix[0][k] = i
            compact_matrix[1][k] = j
            compact_matrix[2][k] = sparseMatrix[i][j]
            k += 1

print(compact_matrix)
