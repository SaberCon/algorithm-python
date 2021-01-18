class Solution:
    def rotatedDigits(self, N: int) -> int:
        N = tuple(map(int, str(N)))

        def count(nums):
            ans = 0
            for i, d in enumerate(N):
                ans += sum(1 for num in nums if num < d) * (len(nums) ** (len(N) - i - 1))
                if d in nums and i == len(N) - 1:
                    ans += 1
                if d not in nums:
                    break
            return ans

        return count((0, 1, 8, 2, 5, 6, 9)) - count((0, 1, 8))
