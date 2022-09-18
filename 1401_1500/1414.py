import bisect


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        nums = [1, 1]
        while nums[-1] < k:
            nums.append(nums[-1] + nums[-2])
        ans = 0
        while k:
            k -= nums[bisect.bisect_right(nums, k) - 1]
            ans += 1
        return ans
