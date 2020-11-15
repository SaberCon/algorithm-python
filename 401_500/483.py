class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        for i in range(len(bin(n)) - 3, 1, -1):
            base = int(n ** (1 / i))
            if base == 1:
                continue
            if sum(base ** j for j in range(i + 1)) == n:
                return str(base)
        return str(n - 1)
