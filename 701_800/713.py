class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0
        ans = 0
        i = 0
        curr = 1
        for j, num in enumerate(nums):
            curr *= num
            while curr >= k:
                curr //= nums[i]
                i += 1
            ans += j - i + 1
        return ans
