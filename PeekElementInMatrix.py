#Find Peek element II
"""
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the 
left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] 
and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
"""
from typing import List
def FindPeekGrid(nums: List[List[int]]) -> List[int]:
    m , n = len(nums) , len(nums[0])
    low , high = 0 , n-1

    def FindMaxIndex(nums: List[List[int]], m: int, n: int, col: int) -> int:
        maxValue , index = -1 , -1
        for i in range(m):
            if maxValue < nums[i][col]:
                maxValue = nums[i][col]
                index = i
        return index

    while low <= high:
        mid = (low+high)//2
        row = FindMaxIndex(nums,m,n,mid)

        left = nums[row][mid-1] if mid - 1 >= 0 else -1
        right = nums[row][mid+1] if mid + 1 < n else -1

        if nums[row][mid] > left and nums[row][mid] > right:
            return [row,mid]
        elif nums[row][mid] < left:
            high = mid - 1
        else:
            low = mid + 1
    return [-1,-1]

matrix = [[10,20,15],[21,30,14],[7,16,32]]
print(FindPeekGrid(matrix))