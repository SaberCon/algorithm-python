class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        if len(nums) > 2:
            nums[1] = '(' + nums[1]
            nums[-1] += ')'
        return '/'.join(nums)
