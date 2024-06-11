# Search a 2D Matrix

"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
"""

def SearchMatrix(arr,target):
    n = len(arr)
    
    def Search(arr):
        for i in range(len(arr)):
            if arr[i] == target:
                return True

    for i in range(n):
        if arr[i][-1] < target:
            continue
        else:
            if Search(arr[i]) == True:
                return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(SearchMatrix(matrix,target))