from collections import Counter


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = Counter()
        counts[0] += 1
        ans = remainder = 0
        for n in nums:
            remainder = (remainder + n) % k
            ans += counts[remainder]
            counts[remainder] += 1
        return ans
