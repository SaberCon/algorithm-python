class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        diffs = {0: [-1]}
        diff = 0
        for i, num in enumerate(nums):
            diff += 1 if num else -1
            diffs.setdefault(diff, [])
            diffs[diff].append(i)
            nums[i] = diff
        return max((i - diffs[num][0] for i, num in enumerate(nums) if num in diffs), default=0)
