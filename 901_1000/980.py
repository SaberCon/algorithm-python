class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        target = 0
        start = 0, 0
        seen = 0

        def dfs(x, y):
            if x < 0 or x >= M or y < 0 or y >= N or grid[x][y] == -1:
                return 0
            nonlocal seen
            b = 1 << (x * N + y)
            if seen & b:
                return 0
            if grid[x][y] == 2:
                return seen == target
            seen |= b
            ans = sum(dfs(dx, dy) for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
            seen ^= b
            return ans

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    start = i, j
                if grid[i][j] == 0 or grid[i][j] == 1:
                    target |= 1 << (i * N + j)
        return dfs(*start)
