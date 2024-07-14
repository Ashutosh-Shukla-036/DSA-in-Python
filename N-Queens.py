from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def isSafe(board, row, col):
            # Check upper left diagonal
            x, y = row, col
            while x >= 0 and y >= 0:
                if board[x][y] == "Q":
                    return False
                x -= 1
                y -= 1
            
            # Check upper right diagonal
            x, y = row, col
            while x >= 0 and y < n:
                if board[x][y] == "Q":
                    return False
                x -= 1
                y += 1
            
            # Check same column
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            
            return True

        def solve(row):
            if row == n:
                # Convert board to list of strings and append to result
                result.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if isSafe(board, row, col):
                    board[row][col] = "Q"
                    solve(row + 1)
                    board[row][col] = "."

        solve(0)
        return result

# Testing the function
n = 4
sol = Solution()
print(sol.solveNQueens(n))
