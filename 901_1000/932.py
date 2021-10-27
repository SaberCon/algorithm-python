from functools import cache


class Solution:

    @cache
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        return [i * 2 for i in self.beautifulArray(n // 2)] + [i * 2 - 1 for i in self.beautifulArray((n + 1) // 2)]
