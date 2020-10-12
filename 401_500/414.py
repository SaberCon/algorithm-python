class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = set()
        for num in nums:
            max_nums.add(num)
            if len(max_nums) > 3:
                max_nums.remove(min(max_nums))
        if len(max_nums) == 3:
            return min(max_nums)
        else:
            return max(max_nums)
