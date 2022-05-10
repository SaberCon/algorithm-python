from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * m for m in rollMax]
        ans = 1
        for _ in range(n):
            for a in dp:
                a.insert(0, (ans - sum(a)) % MOD)
                a.pop()
            ans = sum(sum(a) for a in dp) % MOD
        return ans
