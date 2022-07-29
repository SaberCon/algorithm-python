from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set()
        for n in arr:
            if n in nums:
                return True
            nums.add(n * 2)
            if n % 2 == 0:
                nums.add(n // 2)
        return False
