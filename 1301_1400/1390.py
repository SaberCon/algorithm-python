from collections import Counter
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        nums = Counter(nums)
        size = max(nums)

        bitset = [True] * (size + 1)
        primes = []
        for i in range(2, size + 1):
            if bitset[i]:
                primes.append(i)
                for j in range(2 * i, size + 1, i):
                    bitset[j] = False

        ans = 0
        for p in primes:
            if (num := p ** 3) > size:
                break
            if num in nums:
                ans += (1 + p + p ** 2 + num) * nums[num]
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                if (num := primes[i] * primes[j]) > size:
                    break
                if num in nums:
                    ans += (1 + primes[i] + primes[j] + num) * nums[num]
        return ans
