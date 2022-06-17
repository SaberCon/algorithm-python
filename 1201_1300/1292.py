from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        k = 1
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ps[i][j] = mat[i - 1][j - 1] + ps[i][j - 1] + ps[i - 1][j] - ps[i - 1][j - 1]
                while k <= i and k <= j and ps[i][j] - ps[i - k][j] - ps[i][j - k] + ps[i - k][j - k] <= threshold:
                    k += 1
        return k - 1
