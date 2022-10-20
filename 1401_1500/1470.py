from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[j] for i in range(n) for j in (i, i + n)]
