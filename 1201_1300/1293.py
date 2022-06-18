from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque(((0, 0, 0, k),))
        seen = {(0, 0): k}
        while queue:
            x, y, s, e = queue.popleft()
            if (x, y) == (m - 1, n - 1):
                return s
            for nx, ny in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                ns, ne = s + 1, e
                if grid[nx][ny]:
                    ne -= 1
                if ne >= 0 and ((nx, ny) not in seen or seen[nx, ny] < ne):
                    seen[nx, ny] = ne
                    queue.append((nx, ny, ns, ne))
        return -1
