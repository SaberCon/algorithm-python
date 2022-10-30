class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [i for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
        if k <= len(factors):
            return factors[k - 1]
        k -= len(factors) - (int(n ** 0.5) ** 2 == n)
        return -1 if k > len(factors) else n // factors[-k]
