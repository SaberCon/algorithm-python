class Solution:
    def flipLights(self, n: int, m: int) -> int:
        n = min(n, 3) - 1
        m = min(m, 3)
        return [[1, 1, 1], [2, 3, 4], [2, 4, 7], [2, 4, 8]][m][n]
