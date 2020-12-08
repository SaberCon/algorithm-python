class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        uni_nums = set()
        for num in nums:
            if num in uni_nums:
                duplicate = num
                break
            uni_nums.add(num)
        return duplicate, ((1 + len(nums)) * len(nums) // 2 + duplicate) - sum(nums)
