class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        L = len(strs[0])
        dp = [1] * L
        for i in range(1, L):
            for j in range(i):
                if all(s[j] <= s[i] for s in strs):
                    dp[i] = max(dp[i], 1 + dp[j])
        return L - max(dp)
