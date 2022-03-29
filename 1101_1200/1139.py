class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp1 = [[0] * (N + 1) for _ in range(M + 1)]
        dp2 = [[0] * (N + 1) for _ in range(M + 1)]
        dp3 = [[0] * (N + 1) for _ in range(M + 1)]
        dp4 = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    continue
                dp1[i][j] = dp1[i - 1][j] + 1
                dp2[i][j] = dp2[i][j - 1] + 1
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if grid[i][j] == 0:
                    continue
                dp3[i][j] = dp3[i + 1][j] + 1
                dp4[i][j] = dp4[i][j + 1] + 1

        ans = 0
        for i in range(M):
            for j in range(N):
                for k in range(min(dp1[i][j], dp2[i][j]), ans, -1):
                    if min(dp3[i - k + 1][j - k + 1], dp4[i - k + 1][j - k + 1]) >= k:
                        ans = k
                        break
        return ans * ans
