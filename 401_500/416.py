class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        sum_set = {0}
        for num in nums:
            sum_set |= {i + num for i in sum_set}
            if target in sum_set:
                return True
        return False
