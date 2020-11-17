class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subsequences = [set() for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] >= nums[i]:
                    subsequences[i].add((nums[i], nums[j]))
                    subsequences[i].update(((nums[i],) + sub) for sub in subsequences[j])
        ans = set()
        for subsequence in subsequences:
            ans.update(sub for sub in subsequence)
        return list(ans)
