from collections import Counter
from functools import cache, reduce
from math import factorial


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        N = len(nums)
        duplicate = reduce(lambda x, y: x * factorial(y), Counter(nums).values(), 1)

        squares = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                if ((nums[i] + nums[j]) ** 0.5).is_integer():
                    squares[i].append(j)
                    squares[j].append(i)

        @cache
        def run(num, mask):
            mask |= 1 << num
            if mask == (1 << N) - 1:
                return 1
            return sum(run(n, mask) for n in squares[num] if mask & (1 << n) == 0)

        return sum(run(i, 0) for i in range(N)) // duplicate
