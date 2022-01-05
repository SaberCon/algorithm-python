class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        left = -1
        for i, num in enumerate(nums):
            if num == 0:
                if k > 0:
                    k -= 1
                else:
                    left += 1
                    while left < i and nums[left] == 1:
                        left += 1
            ans = max(ans, i - left)
        return ans
