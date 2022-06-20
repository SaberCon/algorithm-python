from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        nums.sort()
        counter = Counter(nums)
        for n in nums:
            if counter[n] == 0:
                continue
            for num in range(n, n + k):
                if counter[num] == 0:
                    return False
                counter[num] -= 1
        return True
