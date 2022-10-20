from functools import cache
from typing import List


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        balls = [i for i, b in enumerate(balls) for _ in range(b)]
        n = len(balls)

        @cache
        def dp(left: int, right: int, diff: int, i: int, in_left: bool, in_right: bool) -> float:
            if left < 0 or right < 0:
                return 0
            if i == n:
                return int(diff == 0)
            same = i + 1 < n and balls[i] == balls[i + 1]
            add_left = left / (left + right) * dp(left - 1, right, diff + (not in_left), i + 1, same, same and in_right)
            add_right = right / (left + right) * dp(left, right - 1, diff - (not in_right), i + 1, same and in_left, same)
            return add_left + add_right

        return dp(n // 2, n // 2, 0, 0, False, False)
