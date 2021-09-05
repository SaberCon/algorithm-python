from math import gcd


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = a * b // gcd(a, b)
        bot, top = min(a, b), min(a * n, b * n)
        while bot < top:
            mid = (bot + top) // 2
            if mid // a + mid // b - mid // lcm < n:
                bot = mid + 1
            else:
                top = mid
        return bot % (10 ** 9 + 7)
