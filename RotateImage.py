#Rotate Image.

"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise)."""

import numpy as np
import pandas as pd

def Matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

    for i in range(n):
        start = 0
        end = n - 1
        while(start < end):
            matrix[i][start],matrix[i][end] = matrix[i][end],matrix[i][start]
            start += 1
            end -= 1
            
    return matrix

matrix = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
Matrix(matrix)
df = pd.DataFrame(matrix)
print(df.to_string(index=False, header=False))