"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""
from typing import List
from queue import deque

class Node:
    def __init__(self,row,col,distance):
        self.row = row
        self.col = col
        self.distance = distance

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        visited = [[False] * m for _ in range(n)]
        result = [[0] * m for _ in range(n)]

        queue = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append(Node(i,j,0))
                    visited[i][j] = True
        
        deltaRow = [-1,0,1,0]
        deltaCol = [0,1,0,-1]

        while queue:
            current = queue.popleft()
            row , col , distance = current.row , current.col , current.distance

            result[row][col] = distance

            for i in range(4):
                newRow = row + deltaRow[i]
                newCol = col + deltaCol[i]

                if 0 <= newRow < n and 0 <= newCol < m and not visited[newRow][newCol]:
                    queue.append(Node(newRow, newCol, distance + 1))
                    visited[newRow][newCol] = True  

        return result
    
grid = [[0,0,0],[0,1,0],[1,1,1]]
obj = Solution()  
result = obj.updateMatrix(grid)


for row in result:
    print(row)