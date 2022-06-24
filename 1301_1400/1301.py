from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(board)
        dp = [(0, -1)] * n + [(0, 1)]
        for row in board:
            new_dp = [(0, -1)] * (n + 1)
            for i, c in enumerate(row):
                if c == 'X':
                    continue
                last_cells = [(s, p) for s, p in (dp[i], dp[i - 1], new_dp[i - 1]) if p >= 0]
                if not last_cells:
                    continue
                max_sum = max(s for s, _ in last_cells)
                score = 0 if c == 'S' or c == 'E' else int(c)
                new_dp[i] = (max_sum + score, sum(p for s, p in last_cells if s == max_sum) % MOD)
            dp = new_dp
        return [dp[-2][0], max(dp[-2][1], 0)]
