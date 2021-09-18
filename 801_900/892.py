class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def get_junction(i, j):
            return 2 * sum(min(grid[i][j], grid[ni][nj]) for ni, nj in ((i, j + 1), (i + 1, j)) if ni < n and nj < n)

        return sum(grid[i][j] * 4 + 2 - get_junction(i, j) for i in range(n) for j in range(n) if grid[i][j] > 0)
