class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1] * len(word2) for _ in range(len(word1))]

        def min_distance(i1, i2):
            if i1 == len(word1) or i2 == len(word2):
                return max(len(word1) - i1, len(word2) - i2)
            if dp[i1][i2] == -1:
                if word1[i1] == word2[i2]:
                    dp[i1][i2] = min_distance(i1 + 1, i2 + 1)
                else:
                    dp[i1][i2] = min(min_distance(i1 + 1, i2), min_distance(i1, i2 + 1)) + 1
            return dp[i1][i2]

        return min_distance(0, 0)
