class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        islands = [0]

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc

        def dfs(i, j, p):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] <= 0:
                return 0
            grid[i][j] = -p
            return 1 + sum(dfs(r, c, p) for r, c in neighbors(i, j))

        for i in range(n):
            for j in range(n):
                if grid[i][j] <= 0:
                    continue
                islands.append(dfs(i, j, len(islands)))
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    ps = {grid[r][c] for r, c in neighbors(i, j)}
                    ans = max(ans, sum(islands[-p] for p in ps) + 1)
                else:
                    ans = max(ans, islands[-grid[i][j]])
        return ans
