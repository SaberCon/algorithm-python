class Solution:
    def longestDecomposition(self, text: str) -> int:
        N = len(text)

        def dp(left):
            right = N - left
            if left >= right:
                return 0
            for i in range(left + 1, N // 2 + 1):
                if text[left:i] == text[N - i:right]:
                    return 2 + dp(i)
            return 1

        return dp(0)
