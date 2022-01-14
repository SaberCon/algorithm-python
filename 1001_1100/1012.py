from math import factorial


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def f(count, size):
            return factorial(count) // factorial(count - size)

        nums = [int(c) for c in str(n)]
        N = len(nums)
        ans = sum(9 * f(9, i) for i in range(N - 1))
        seen = [False] * 10
        for i, num in enumerate(nums):
            for j in range(num):
                if seen[j] or (i == j == 0):
                    continue
                ans += f(9 - i, N - i - 1)
            if seen[num]:
                break
            seen[num] = True
        else:
            ans += 1
        return n - ans
