from collections import defaultdict
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        def equal_freq(counts: defaultdict) -> bool:
            if len(counts) == 1:
                return 1 in counts.keys() or 1 in counts.values()
            if len(counts) == 2:
                min_key, max_key = sorted(counts.keys())
                return (min_key == 1 and counts[min_key] == 1) or (max_key - min_key == 1 and counts[max_key] == 1)
            return False

        occurrences = defaultdict(lambda: 0)
        counts = defaultdict(lambda: 0)
        ans = 0
        for i, n in enumerate(nums):
            o = occurrences[n]
            occurrences[n] = o + 1
            counts[o] -= 1
            if counts[o] < 1:
                del counts[o]
            counts[o + 1] += 1
            if equal_freq(counts):
                ans = i + 1
        return ans
