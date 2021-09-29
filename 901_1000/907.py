class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = [(-1, 0)]
        dp = 0
        ans = 0
        for i, n in enumerate(arr):
            diff = n
            while stack[-1][1] >= n:
                li, ln = stack.pop()
                diff -= (ln - n) * (li - stack[-1][0])
            stack.append((i, n))
            dp += diff
            ans = (ans + dp) % MOD
        return ans
