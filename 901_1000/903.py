class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        memo = {}

        def dp(i, j):
            if i == n:
                return 1
            if (s[i] == 'I' and j == n - i) or (s[i] == 'D' and j == 0):
                return 0
            if (i, j) in memo:
                return memo[i, j]
            if s[i] == 'I':
                memo[i, j] = (dp(i, j + 1) + dp(i + 1, j)) % MOD
            if s[i] == 'D':
                memo[i, j] = (dp(i, j - 1) + dp(i + 1, j - 1)) % MOD
            return memo[i, j]

        return sum(dp(0, i) for i in range(n + 1)) % MOD
