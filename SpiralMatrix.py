#Spiral Mtarix

#Given an m x n matrix, return all elements of the matrix in spiral order.

import numpy as np
import pandas as pd

def SprialMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    left , top = 0 , 0
    right , bottom = m-1 , n-1
    result = []

    while(top <= bottom and left <= right):
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right -= 1

        if(top <= bottom):
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if(left <= right):
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left += 1

    return result

matrix = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])

dp = pd.DataFrame(matrix)
print(dp.to_string(index=False,header=False))
print()
print(SprialMatrix(matrix))

#Time complexity O(mxn)