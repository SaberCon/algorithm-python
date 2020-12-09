class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '^#' + '#'.join(s) + '#$'
        dp = [0] * len(s)
        ans = m = 0
        for i in range(1, len(s) - 1):
            dp[i] = 0 if m + dp[m] <= i else min(m + dp[m] - i, dp[2 * m - i])
            while s[i + dp[i] + 1] == s[i - dp[i] - 1]:
                dp[i] += 1
            if i + dp[i] >= m + dp[m]:
                m = i
            ans += (dp[i] + 1) // 2
        return ans
