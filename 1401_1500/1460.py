from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return all(t == a for t, a in zip(sorted(target), sorted(arr)))
