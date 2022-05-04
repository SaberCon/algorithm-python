from collections import deque
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        N = len(grid)
        seen = {(0, 0, True)}

        def is_valid(x, y):
            return 0 <= x < N and 0 <= y < N and grid[x][y] != 1

        queue = deque(((0, 0, True, 0),))
        while queue:
            x, y, d, m = queue.popleft()

            for next_item in ((x, y, not d), (x + 1, y, d), (x, y + 1, d)):
                nx, ny, nd = next_item
                if is_valid(nx, ny) and is_valid(nx + 1 - nd, ny + nd) and (d == nd or is_valid(nx + 1, ny + 1)) \
                        and next_item not in seen:
                    if next_item == (N - 1, N - 2, True):
                        return m + 1
                    queue.append((nx, ny, nd, m + 1))
                    seen.add(next_item)
        return -1
