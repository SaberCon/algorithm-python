class Solution:
    def countSubstrings(self, s: str) -> int:
        old_dp, dp = [0] * len(s), [1] * len(s)
        old_palindrome, palindrome = [1] * len(s), [1] * len(s)
        for i in range(1, len(s)):
            new_dp = []
            new_palindrome = []
            for j in range(0, len(s) - i):
                new_palindrome.append(1 if s[j] == s[j + i] and old_palindrome[j + 1] else 0)
                new_dp.append(dp[j] + dp[j + 1] - old_dp[j + 1] + new_palindrome[-1])
            old_dp, dp = dp, new_dp
            old_palindrome, palindrome = palindrome, new_palindrome
        return dp[0]
