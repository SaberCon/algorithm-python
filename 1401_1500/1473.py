from functools import cache
from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        max_cost = 10 ** 9
        for i in range(len(houses)):
            houses[i] -= 1

        @cache
        def dp(house: int, color: int, num: int) -> int:
            if house >= m:
                return 0 if num == 0 else max_cost
            if num < 0:
                return max_cost
            if houses[house] >= 0:
                return dp(house + 1, houses[house], num - (houses[house] != color))
            return min(
                cost[house][color] + dp(house + 1, color, num) if color < n else max_cost,
                [v for c, v in min_cost(house, num) if c != color][0]
            )

        @cache
        def min_cost(house: int, num: int) -> List[List[int]]:
            min_cost1 = min_cost2 = [-1, max_cost]
            for i, c in enumerate(cost[house]):
                current_cost = c + dp(house + 1, i, num - 1)
                if current_cost < min_cost1[1]:
                    min_cost1, min_cost2 = [i, current_cost], min_cost1
                elif current_cost < min_cost2[1]:
                    min_cost2 = [i, current_cost]
            return [min_cost1, min_cost2]

        ans = dp(0, n, target)
        return ans if ans < max_cost else -1
