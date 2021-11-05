class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        last = -1
        for num in nums:
            if num > last:
                last = num
            else:
                ans += last - num + 1
                last += 1
        return ans
