def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(0)
        transposed.append(row)
    
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transposed[i][j] = matrix[j][i]
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]   
transposed_matrix = transpose(matrix)
print(transposed_matrix)
