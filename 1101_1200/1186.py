class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp1 = dp2 = ans = -100000
        for n in arr:
            dp1, dp2 = max(n, n + dp1), max(n, n + dp2, dp1)
            ans = max(ans, dp2)
        return ans
