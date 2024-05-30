#Set Matrix Zero

"""Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and 
then return the matrix or modify a original matrix
Example:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]].
"""


import numpy as np
import pandas as pd

#Brute Force .
def Matrix(matrix):
    def row(i):
        for j in range(len(matrix[0])):
            if(matrix[i][j] != 0):
                matrix[i][j] = -1

    def col(j):
        for i in range(len(matrix)):
            if(matrix[i][j] != 0):
                matrix[i][j] = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 0):
                row(i)
                col(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == -1):
                matrix[i][j] = 0

matrix = np.array([
    [1,1,1,],
    [1,0,1,],
    [1,1,1,]
])

Matrix(matrix)
df = pd.DataFrame(matrix)
print(df.to_string(index=False,header=False))
#Time compexity of O(2(M*N)) + O(M+N) Not god at all go for optimal solution
print("-------------------------------------------------")

#optimal method with time complexity of O(M*N) + O(M*N) and space complexity of O(N)+O(M)
def SetMatrix(matrix):
    rlen = len(matrix)
    clen = len(matrix[0])
    row = [0] * rlen
    col = [0] * clen

    for i in range(rlen):
        for j in range(clen):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(rlen):
        for j in range(clen):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0


matrix = np.array([
    [1,1,1,],
    [1,0,1,],
    [1,1,1,]
])

SetMatrix(matrix)
df = pd.DataFrame(matrix)
print(df.to_string(index=False,header=False))