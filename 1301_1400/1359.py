class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        ans = 1
        for i in range(1, n + 1):
            ans = ans * (2 * i - 1) * i % mod
        return ans
