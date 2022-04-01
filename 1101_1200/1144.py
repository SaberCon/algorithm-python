class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        N = len(nums)
        nums.append(10000)
        even = sum(max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1) for i in range(0, N, 2))
        odd = sum(max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1) for i in range(1, N, 2))
        return min(even, odd)
