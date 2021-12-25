from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        queue = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        ans = 0
        while queue:
            i, j, t = queue.popleft()
            ans = t
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    queue.append((ni, nj, t + 1))
        return ans if all(1 not in row for row in grid) else -1
