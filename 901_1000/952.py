from collections import Counter


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [i for i in range(N)]

        def find_root(i):
            return i if dp[i] == i else find_root(dp[i])

        def set_root(i, n):
            m = dp[i]
            dp[i] = n
            if dp[i] != i:
                set_root(m, n)

        factors = {}
        for i, num in enumerate(nums):
            for j in range(1, int(num ** 0.5) + 1):
                if num % j == 0:
                    if j != 1 and j in factors:
                        set_root(factors[j], i)
                    if num / j != 1 and num / j in factors:
                        set_root(factors[num / j], i)
                    factors[j] = i
                    factors[num / j] = i

        return max(Counter(find_root(i) for i in range(N)).values())
