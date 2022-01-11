from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = Counter()
        ans = 0
        for t in time:
            r = t % 60
            ans += count[-r % 60]
            count[r] += 1
        return ans
