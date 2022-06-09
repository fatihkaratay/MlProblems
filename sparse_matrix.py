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
