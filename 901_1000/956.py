class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        top = sum(rods) // 2
        dp = [0] + [-1] * top
        for r in rods:
            new_dp = dp.copy()
            for i, s in enumerate(dp):
                if s < 0:
                    continue
                for diff, size in ((i + r, s + r), (abs(i - r), max(s, s - i + r))):
                    if diff <= top:
                        new_dp[diff] = max(new_dp[diff], size)
            dp = new_dp
        return dp[0]
