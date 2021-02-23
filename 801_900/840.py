class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] != 5:
                    continue
                a, b, c, d, e, f, g, h = grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1], grid[i][j + 1], \
                                         grid[i + 1][j + 1], grid[i + 1][j], grid[i + 1][j - 1], grid[i][j - 1]
                if {a, c, e, g} != {2, 4, 6, 8} or {b, d, f, h} != {1, 3, 7, 9}:
                    continue
                if not all(grid[i + di][j + dj] + grid[i - di][j - dj] == 10 for di, dj in
                           ((0, 1), (1, 0), (1, 1), (1, -1))):
                    continue
                if not all(n1 + n2 + n3 == 15 for n1, n2, n3 in ((a, b, c), (c, d, e), (e, f, g), (g, h, a))):
                    continue
                ans += 1
        return ans
