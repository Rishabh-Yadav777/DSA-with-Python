class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = '0'

            while stack:
                x, y = stack.pop()

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dx, dy in directions:
                    nr = x + dx
                    nc = y + dy

                    if (0 <= nr < rows and 0 <= nc < cols
                            and grid[nr][nc] == '1'):
                        grid[nr][nc] = '0'
                        stack.append((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count