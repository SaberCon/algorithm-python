from collections import defaultdict
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_dict = defaultdict(set)
        for i, n in enumerate(nums):
            num_dict[n].add(i)
        count = 0
        ans = [0] * len(nums)
        for n, s in sorted(num_dict.items()):
            for i in s:
                ans[i] = count
            count += len(s)
        return ans
