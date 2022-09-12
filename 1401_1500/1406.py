from functools import cache
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def dp(i: int) -> int:
            return max((sum(stoneValue[i:j + 1]) - dp(j + 1) for j in range(i, min(i + 3, len(stoneValue)))), default=0)

        score = dp(0)
        return "Alice" if score > 0 else "Bob" if score < 0 else "Tie"
