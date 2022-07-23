from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total = 0
        for i, (_, num) in enumerate(Counter(arr).most_common()):
            total += num
            if total >= len(arr) // 2:
                return i + 1
