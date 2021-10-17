class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        for i in range(0, len(nums) // 2, 2):
            nums[i], nums[-i - 1] = nums[-i - 1], nums[i]
        return nums
