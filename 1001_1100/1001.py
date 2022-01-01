from collections import Counter


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamps = set((x, y) for x, y in lamps)
        rows, columns, diagonals1, diagonals2 = Counter(), Counter(), Counter(), Counter()
        for x, y in lamps:
            rows[x] += 1
            columns[y] += 1
            diagonals1[x - y] += 1
            diagonals2[x + y] += 1
        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            if rows[x] > 0 or columns[y] > 0 or diagonals1[x - y] > 0 or diagonals2[x + y] > 0:
                ans[i] = 1
            for nx in range(max(x - 1, 0), min(x + 2, n)):
                for ny in range(max(y - 1, 0), min(y + 2, n)):
                    if (nx, ny) in lamps:
                        lamps.remove((nx, ny))
                        rows[nx] -= 1
                        columns[ny] -= 1
                        diagonals1[nx - ny] -= 1
                        diagonals2[nx + ny] -= 1
        return ans
