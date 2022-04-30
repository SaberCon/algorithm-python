from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = Counter(arr).values()
        return len(occurrences) == len(set(occurrences))
