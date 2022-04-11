from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque()
        seen = set()
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    seen.add((i, j))
                    queue.append((i, j, 0))
        ans = 0
        while queue:
            i, j, d = queue.popleft()
            ans = d
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    queue.append((ni, nj, d + 1))
        return ans if ans else -1
