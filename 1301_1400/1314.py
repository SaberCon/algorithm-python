from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + mat[i][j]
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                min_r, max_r, min_c, max_c = max(0, i - k), min(m, i + k + 1), max(0, j - k), min(n, j + k + 1)
                ans[i][j] = ps[max_r][max_c] + ps[min_r][min_c] - ps[min_r][max_c] - ps[max_r][min_c]
        return ans
