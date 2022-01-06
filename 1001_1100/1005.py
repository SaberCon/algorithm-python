class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i, n in enumerate(nums):
            if n >= 0:
                break
            nums[i] = -n
            k -= 1
            if k == 0:
                break
        return sum(nums) if k % 2 == 0 else sum(nums) - 2 * min(nums[i], nums[i - 1])
