class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            if row[0] == 0:
                grid[i] = [1 - v for v in row]
        n = len(grid[0]) - 1
        return sum(max(col.count(0), col.count(1)) * (2 ** (n - i)) for i, col in enumerate(zip(*grid)))
