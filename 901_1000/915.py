class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        mis = [10 ** 7] * (N + 1)
        for i in range(N - 1, -1, -1):
            mis[i] = min(mis[i + 1], nums[i])
        ma = 0
        for i, n in enumerate(nums):
            ma = max(ma, n)
            if ma <= mis[i + 1]:
                return i + 1
        return -1
