class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            num = abs(num) - 1
            nums[num] = -abs(nums[num])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
