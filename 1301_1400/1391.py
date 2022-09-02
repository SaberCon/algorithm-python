from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True
        streets = (((0, 1), (0, -1)), ((1, 0), (-1, 0)), ((0, -1), (1, 0)),
                   ((0, 1), (1, 0)), ((0, -1), (-1, 0)), ((0, 1), (-1, 0)))
        for x, y in ((0, 1), (1, 0)):
            if (x, y) not in streets[grid[0][0] - 1]:
                continue
            seen = {(0, 0)}
            dx, dy = x, y
            while 0 <= x < m and 0 <= y < n and (x, y) not in seen and (-dx, -dy) in streets[grid[x][y] - 1]:
                if x == m - 1 and y == n - 1:
                    return True
                seen.add((x, y))
                dx, dy = next(filter(lambda d: d != (-dx, -dy), streets[grid[x][y] - 1]))
                x += dx
                y += dy
        return False
