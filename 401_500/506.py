class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ans = [""] * len(nums)
        for i, (_, index) in enumerate(sorted((-num, i) for i, num in enumerate(nums))):
            if i < len(medals):
                ans[index] = medals[i]
            else:
                ans[index] = str(i + 1)
        return ans
