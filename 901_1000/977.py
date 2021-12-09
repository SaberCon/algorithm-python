from bisect import bisect_left


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        mid = bisect_left(nums, 0)
        neg, pos = mid - 1, mid
        nums.append(100000)
        ans = []
        while neg >= 0 or pos < N:
            n = nums[neg] ** 2
            p = nums[pos] ** 2
            if n < p:
                ans.append(n)
                neg -= 1
            else:
                ans.append(p)
                pos += 1
        return ans
