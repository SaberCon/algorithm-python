class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        mines = {(i, j) for i, j in mines}
        dp = [[[0] * 4 for _ in range(N)] for _ in range(N)]
        for p, (di, dj) in enumerate(((1, 0), (0, 1), (-1, 0), (0, -1))):
            for i in range(N) if di < 0 else range(N - 1, -1, -1):
                for j in range(N) if dj < 0 else range(N - 1, -1, -1):
                    if (i, j) in mines:
                        continue
                    dp[i][j][p] = 1
                    if 0 <= i + di < N and 0 <= j + dj < N:
                        dp[i][j][p] += dp[i + di][j + dj][p]
        return max(min(s) for row in dp for s in row)
