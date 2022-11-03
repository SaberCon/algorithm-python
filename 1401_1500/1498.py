from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        exp2 = [1] * n
        for i in range(1, n):
            exp2[i] = 2 * exp2[i - 1] % MOD

        nums.sort()
        j = n - 1
        ans = 0
        for i, num in enumerate(nums):
            if num * 2 > target:
                break
            while num + nums[j] > target:
                j -= 1
            ans = (ans + exp2[j - i]) % MOD
        return ans
