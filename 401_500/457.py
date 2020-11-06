class Solution:
    def circularArrayLoop(self, nums: [int]) -> bool:
        for i in range(len(nums)):
            curr = i
            plus = nums[i] > 0
            sign = 10000 - i
            while abs(nums[curr]) % len(nums) != 0 and nums[curr] < sign and (nums[curr] > 0) == plus:
                temp = nums[curr]
                nums[curr] = sign
                curr = (curr + temp) % len(nums)
                if nums[curr] == sign:
                    return True
        return False
