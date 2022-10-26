from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = sorted(Counter(arr).values())
        ans = len(counts)
        for count in counts:
            if count > k:
                break
            k -= count
            ans -= 1
        return ans
