class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda c: c[0] - c[1])
        N = len(costs) // 2
        return sum(cost[0] for cost in costs[:N]) + sum(cost[1] for cost in costs[N:])
