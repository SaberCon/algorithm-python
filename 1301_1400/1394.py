from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        return max((num for num in counter if counter[num] == num), default=-1)
