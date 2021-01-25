class Solution:
    def hitBricks(self, grid: [[int]], hits: [[int]]) -> [int]:
        for x, y in hits:
            if grid[x][y] == 1:
                grid[x][y] = -1

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
                return 0
            grid[x][y] = 2
            return sum(dfs(x + dx, y + dy) for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1))) + 1

        for i in range(len(grid[0])):
            dfs(0, i)

        ans = []
        for x, y in reversed(hits):
            ans.append(0)
            if grid[x][y] == 0:
                continue
            grid[x][y] = 1
            if x == 0 or any(0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 2
                             for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1))):
                ans[-1] = dfs(x, y) - 1
        return list(reversed(ans))
