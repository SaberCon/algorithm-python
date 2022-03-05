from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque(((-1, -1, 0),))
        while queue:
            x, y, s = queue.popleft()
            for nx in range(x - 1, x + 2):
                for ny in range(y - 1, y + 2):
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                        if nx == N - 1 and ny == N - 1:
                            return s + 1
                        grid[nx][ny] = 1
                        queue.append((nx, ny, s + 1))
        return -1
