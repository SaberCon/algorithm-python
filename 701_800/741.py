class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        size = len(grid)
        dp = [[-1] * size for _ in range(size)]
        dp[0][0] = grid[0][0]
        for s in range(1, 2 * size - 1):
            new_dp = [[-1] * size for _ in range(size)]
            for i in range(max(0, s - size + 1), min(s + 1, size)):
                for j in range(max(0, s - size + 1), min(s + 1, size)):
                    if grid[i][s - i] == -1 or grid[j][s - j] == -1:
                        continue
                    for di, dj in (0, 0), (-1, 0), (0, -1), (-1, -1):
                        if dp[i + di][j + dj] == -1:
                            continue
                        new_dp[i][j] = max(new_dp[i][j], dp[i + di][j + dj] +
                                           (grid[i][s - i] if i == j else grid[i][s - i] + grid[j][s - j]))
            dp = new_dp
        return max(dp[-1][-1], 0)
