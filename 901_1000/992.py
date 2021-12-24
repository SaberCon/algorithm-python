class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarray_with_k_at_most(nums, k):
            if k == 0:
                return 0
            N = len(nums)
            counter = [0] * (N + 1)
            count = end = ans = 0
            for i, num in enumerate(nums):
                while end < N and (count < k or counter[nums[end]] > 0):
                    counter[nums[end]] += 1
                    if counter[nums[end]] == 1:
                        count += 1
                    end += 1
                ans += end - i
                counter[num] -= 1
                if counter[num] == 0:
                    count -= 1
            return ans

        return subarray_with_k_at_most(nums, k) - subarray_with_k_at_most(nums, k - 1)
