class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        nums = [0] * 10
        for i in range(10):
            num = i * k
            nums[num % 10] = num
        ans = 0
        while k:
            k = (k + nums[(1 - k % 10) % 10]) // 10
            ans += 1
        return ans
