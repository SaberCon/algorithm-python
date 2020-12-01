class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        ans = 0
        for num, count in counts.items():
            for i in (1, -1):
                if num + i in counts:
                    ans = max(ans, count + counts[num + i])
        return ans
