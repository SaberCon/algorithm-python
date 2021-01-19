class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def count_zero(num):
            ans = 0
            while num // 5:
                num //= 5
                ans += num
            return ans

        l, r = 0, 5 * (10 ** 9)
        while l <= r:
            m = (l + r) // 2
            count = count_zero(m)
            if count == K:
                return 5
            if count < K:
                l = m + 1
            else:
                r = m - 1
        return 0
