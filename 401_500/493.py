class Solution:
    def reversePairs(self, nums: [int]) -> int:
        for num in nums:
            


# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
print(Solution().reversePairs([1, 3, 2, 3, 1]))  # 2
print(Solution().reversePairs([2, 4, 3, 5, 1]))  # 3
