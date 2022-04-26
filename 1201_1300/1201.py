from math import lcm


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left, right = 1, min(2 * 10 ** 9, min(a, b, c) * n)
        ab, bc, ac, abc = lcm(a, b), lcm(b, c), lcm(a, c), lcm(a, b, c)
        while left < right:
            m = (left + right) // 2
            if m // a + m // b + m // c - m // ab - m // bc - m // ac + m // abc < n:
                left = m + 1
            else:
                right = m
        return left
