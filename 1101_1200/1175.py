import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return n != 1

        prime_num = sum(is_prime(i + 1) for i in range(n))
        return math.factorial(prime_num) * math.factorial(n - prime_num) % (10 ** 9 + 7)
