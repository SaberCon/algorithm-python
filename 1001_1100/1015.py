class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 10 not in (1, 3, 7, 9):
            return -1
        nums = [0] * 10
        for i in range(10):
            num = i * k
            nums[num % 10] = num
        ans = 0
        seen = set()
        while k:
            if k in seen:
                return -1
            seen.add(k)
            k = (k + nums[(1 - k % 10) % 10]) // 10
            ans += 1
        return ans
