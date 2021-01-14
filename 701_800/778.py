import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        m = len(grid)
        seen = {(0, 0)}
        while heap:
            h, i, j = heapq.heappop(heap)
            if i == j == m - 1:
                return h
            for i, j in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= i < m and 0 <= j < m and (i, j) not in seen:
                    heapq.heappush(heap, (max(h, grid[i][j]), i, j))
                    seen.add((i, j))
