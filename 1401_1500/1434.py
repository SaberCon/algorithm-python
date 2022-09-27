from functools import cache
from typing import List


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        hat_people = [[0] for _ in range(40)]
        for p, preferred_hats in enumerate(hats):
            for h in preferred_hats:
                hat_people[h - 1].append(1 << p)

        @cache
        def dp(hat: int, wear_mask: int) -> int:
            if hat >= 40:
                return wear_mask + 1 == (1 << n)
            return sum(dp(hat + 1, p | wear_mask) for p in hat_people[hat] if p & wear_mask == 0) % 1000000007

        return dp(0, 0)
