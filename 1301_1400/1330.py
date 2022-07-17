from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        if (n := len(nums)) < 2:
            return 0
        ans = raw = sum(abs(nums[i] - nums[i + 1]) for i in range(n - 1))
        top, bot = min(nums[0], nums[1]), max(nums[0], nums[1])
        for i in range(1, n - 1):
            ans = max(ans, raw + abs(nums[i + 1] - nums[0]) - abs(nums[i + 1] - nums[i]))
            ans = max(ans, raw + abs(nums[i - 1] - nums[n - 1]) - abs(nums[i - 1] - nums[i]))
            ma, mi = max(nums[i], nums[i + 1]), min(nums[i], nums[i + 1])
            if ma < top:
                ans = max(ans, raw + 2 * (top - ma))
            if mi > bot:
                ans = max(ans, raw + 2 * (mi - bot))
            top, bot = max(top, mi), min(bot, ma)
        return ans
