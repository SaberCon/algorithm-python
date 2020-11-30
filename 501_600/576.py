class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        mod = 10 ** 9 + 7
        cache = {}

        def find_path(i, j, N):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if N == 0:
                return 0
            if (i, j, N) not in cache:
                cache[i, j, N] = sum(
                    find_path(i + di, j + dj, N - 1) for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0))) % mod
            return cache[i, j, N]

        return find_path(i, j, N)
