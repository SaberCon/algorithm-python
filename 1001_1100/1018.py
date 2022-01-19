class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        r = 0
        for num in nums:
            r = (r * 2 + num) % 5
            ans.append(r == 0)
        return ans
