from math import gcd


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = p * q // gcd(p, q)
        if lcm // p % 2 == 0:
            return 0
        return 1 if lcm // q % 2 else 2
