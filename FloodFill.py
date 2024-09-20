#Flood Fill Algorithm

"""
Given a 2D array representing an image, a starting pixel (sr, sc), and a new color, implement a function to perform
a flood fill on the image. The function should change the color of the starting pixel and all connected pixels 
with the same color to the new color.
"""
from typing import List

def FloodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    n , m = len(image) , len(image[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    delRow = [-1,0,1,0]
    delCol = [0,1,0,-1]

    def DFS(sr: int, sc: int) -> None:
        connected = image[sr][sc]
        visited[sr][sc] = True
        image[sr][sc] = color

        for i in range(4):
            newRow = delRow[i] + sr
            newCol = delCol[i] + sc
            if((0 <= newRow < n) and (0 <= newCol < m) and (image[newRow][newCol] == connected) and not visited[newRow][newCol]):
                DFS(newRow,newCol)

    DFS(sr,sc)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]] 
sr = 1
sc = 1
color = 2
print(FloodFill(image,sr,sc,color))