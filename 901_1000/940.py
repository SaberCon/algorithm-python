class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] * (len(s) + 1)
        counts = [0] * 26
        for i, c in enumerate(s):
            dp[i + 1] = (2 * dp[i] - counts[ord(c) - ord('a')]) % MOD
            counts[ord(c) - ord('a')] = dp[i]
        return (dp[-1] - 1) % MOD
