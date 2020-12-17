class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            new_dp = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if dp[i][j] <= 0:
                        continue
                    for di, dj in ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)):
                        if 0 <= i + di < N and 0 <= j + dj < N:
                            new_dp[i + di][j + dj] += dp[i][j]
            dp = new_dp
        return sum(sum(row) for row in dp) / 8 ** K
