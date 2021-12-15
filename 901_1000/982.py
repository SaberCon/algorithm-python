class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        counts = [0] * (max(nums) + 1)
        ans = 0
        for i, n in enumerate(nums):
            if n == 0:
                ans += 1
            for d, c in enumerate(counts):
                if c > 0 and d & n == 0:
                    ans += 6 * c
            for j in range(i):
                double = n & nums[j]
                counts[double] += 1
                if double == 0:
                    ans += 6
        return ans
