from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M, N = len(matrix), len(matrix[0])
        ps = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                ps[i][j] = matrix[i - 1][j - 1] + ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]
        ans = 0
        for i in range(M):
            for j in range(i + 1, M + 1):
                counter = defaultdict(lambda: 0)
                for k in range(N + 1):
                    s = ps[j][k] - ps[i][k]
                    ans += counter[s - target]
                    counter[s] += 1
        return ans
