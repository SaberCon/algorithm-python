class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 0
        return ans
