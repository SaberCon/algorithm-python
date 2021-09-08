class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(1 for row in grid for n in row if n) + sum(max(row) for row in grid) \
               + sum(max(col) for col in zip(*grid))
