class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] == 0:
                return
            grid[i][j] = 0
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                dfs(i + di, j + dj)

        for i in (0, M - 1):
            for j in range(N):
                dfs(i, j)

        for j in (0, N - 1):
            for i in range(M):
                dfs(i, j)

        return sum(sum(row) for row in grid)
