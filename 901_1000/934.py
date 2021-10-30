from collections import deque


class Solution:
    def shortestBridge(self, grid: [[int]]) -> int:
        N = len(grid)
        seen = set()
        queue = deque()

        def init(x, y):
            if grid[x][y] == 0:
                queue.append((x, y, 0))
            else:
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        init(nx, ny)

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    seen.add((i, j))
                    init(i, j)
                    break
            if seen:
                break

        while queue:
            x, y, c = queue.popleft()
            if grid[x][y] == 1:
                return c
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append((nx, ny, c + 1))
