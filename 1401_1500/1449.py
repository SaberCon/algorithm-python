from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cost = [(i + 1, c) for i, c in enumerate(cost)][::-1]
        dp = [(0, 0)] * (target + 1)
        for i in range(1, target + 1):
            num, size = -1, 0
            for j, c in cost:
                if i - c >= 0 and dp[i - c][0] >= 0 and dp[i - c][1] + 1 > size:
                    num, size = j, dp[i - c][1] + 1
            dp[i] = (num, size)

        if dp[target][0] < 0:
            return '0'
        ans = []
        while target:
            num = dp[target][0]
            ans.append(str(num))
            target -= cost[9 - num][1]
        return ''.join(ans)
