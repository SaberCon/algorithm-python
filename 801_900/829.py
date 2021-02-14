class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        return sum(1 for i in range(1, int((2 * N) ** 0.5) + 1)
                   if (i % 2 and not N % i) or (not i % 2 and not (N - i / 2) % i))
