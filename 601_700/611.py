class Solution:
    def triangleNumber(self, nums: [int]) -> int:
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            left, right = i + 1, i + 2
            while right < len(nums):
                if num + nums[left] > nums[right]:
                    ans += right - left
                    right += 1
                else:
                    left += 1
                    if left == right:
                        right += 1
        return ans
