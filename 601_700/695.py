class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0

        def find_area(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            nonlocal ans, curr
            grid[i][j] = 0
            curr += 1
            ans = max(ans, curr)
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                find_area(i + di, j + dj)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = 0
                find_area(i, j)
        return ans
