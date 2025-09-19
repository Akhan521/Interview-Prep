'''
Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. 
The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

def transpose(matrix):
    pass
    
Example Usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)

Example Output:
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
[
    [1, 4],
    [2, 5],
    [3, 6]
]
'''

def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    
    for r in range(rows): 
        for c in range(cols): 
            result[c][r] = matrix[r][c]

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))




            
