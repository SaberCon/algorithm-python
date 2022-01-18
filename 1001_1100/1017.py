class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        ans = ''
        while n:
            n, mod = -(n >> 1), n % 2
            ans += str(mod)
        return ans[::-1]
