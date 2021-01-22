class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        limit_x = [max(row) for row in grid]
        limit_y = [max(row) for row in zip(*grid)]
        return sum(min(limit_x[i], limit_y[j]) - grid[i][j] for i in range(len(grid)) for j in range(len(grid)))
