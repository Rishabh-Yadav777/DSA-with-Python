from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m = len(board)
        n = len(board[0])

        stack = []

        # Find all 'O's on the boundary
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    stack.append((i, j))

        for j in range(n):
            for i in [0, m - 1]:
                if board[i][j] == 'O':
                    stack.append((i, j))

        # Mark boundary-connected 'O's as safe
        while stack:
            i, j = stack.pop()

            if board[i][j] != 'O':
                continue

            board[i][j] = '#'

            for x, y in [(i - 1, j), (i + 1, j),
                         (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n:
                    if board[x][y] == 'O':
                        stack.append((x, y))

        # Capture surrounded regions and restore safe cells
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'