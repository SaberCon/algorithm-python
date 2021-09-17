class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = (10 ** 9 + 7)
        nums.sort()
        ans = 0
        last_sum = 0
        last_pow = 1
        for i in range(1, len(nums)):
            last_pow = last_pow * 2 % MOD
            last_sum = (last_sum * 2 + (nums[i] - nums[i - 1]) * (last_pow - 1)) % MOD
            ans = (ans + last_sum) % MOD
        return ans
