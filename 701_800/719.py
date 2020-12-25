class Solution:
    def smallestDistancePair(self, nums: [int], k: int) -> int:
        nums.sort()
        l, r = min(n2 - n1 for n1, n2 in zip(nums, nums[1:])), nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            count = 0
            e = 1
            for s in range(len(nums) - 1):
                while e < len(nums) and nums[e] - nums[s] <= mid:
                    e += 1
                count += e - s - 1
            if count < k:
                l = mid + 1
            else:
                r = mid
        return l
