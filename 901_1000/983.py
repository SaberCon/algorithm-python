class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 400
        last_index = 0
        last_cost = 0
        for day in days:
            for i in range(last_index, day):
                dp[i] = last_cost
            last_index = day
            last_cost = min(costs[0] + dp[day - 1], costs[1] + dp[day - 7], costs[2] + dp[day - 30])
        return last_cost
