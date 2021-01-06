class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]
        for c in cost[2:]:
            dp.append(c + min(dp[-1], dp[-2]))
        return min(dp[-1], dp[-2])
