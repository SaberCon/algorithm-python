from functools import cache
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @cache
        def min_difficulty(start: int, d: int) -> int:
            if d == 1:
                return max(jobDifficulty[start:])
            difficulty = 0
            ans = 10000
            for i in range(start, n - d + 1):
                difficulty = max(difficulty, jobDifficulty[i])
                ans = min(ans, difficulty + min_difficulty(i + 1, d - 1))
            return ans

        return min_difficulty(0, d)
