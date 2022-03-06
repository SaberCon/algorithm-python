class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N1, N2 = len(str1), len(str2)
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        for i in range(N1):
            for j in range(N2):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        ans = []
        i, j = N1, N2
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                ans.append(str1[i - 1])
                i -= 1
            else:
                ans.append(str2[j - 1])
                j -= 1
        return str1[:i] + str2[:j] + ''.join(reversed(ans))
