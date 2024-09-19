#Number of Provinces

"""
A province is a group of cities that are directly or indirectly connected. You are given an n x n matrix 
isConnected where isConnected[i][j] is 1 if the i-th city is directly connected to the j-th city, and 0 otherwise.

You need to find the number of provinces in the given matrix. A province is a group of cities that are directly 
or indirectly connected. Two cities belong to the same province if there is a path between them in the matrix.

Input :
An n x n integer matrix isConnected where 1 <= n <= 100 and isConnected[i][j] is either 0 or 1. The matrix is 
symmetric (i.e., isConnected[i][j] is equal to isConnected[j][i]), and isConnected[i][i] is always 1.

Output:
An integer representing the number of provinces (connected components) in the matrix.

Solution:
Use Depth-First Search (DFS) or Breath First Serach (BFS) to traverse all cities connected to a starting city, 
marking them as visited. Count the number of times a new DFS is initiated, which represents the number of 
distinct provinces.
"""
from typing import List

def NP(isConnected: List[List[int]]) -> int:
    n , count = len(isConnected) , 0
    visited = [False] * n

    def DFS(start: int) -> None:
        visited[start] = True

        for i in range(n):
            if isConnected[start][i] == 1 and not visited[i]:
                DFS(i)

    for i in range(n):
        if not visited[i]:
            count += 1
            DFS(i)

    return count

isConnected = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1]
]

print(NP(isConnected))