class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return sum(i + di < 0 or i + di >= len(grid) or j + dj < 0 or j + dj >= len(grid[0]) or grid[i + di][j + dj] == 0
                   for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0))
                   for j in range(0, len(grid[0])) for i in range(0, len(grid)) if grid[i][j] > 0)
