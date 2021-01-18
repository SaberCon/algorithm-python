class Solution:
    def numTilings(self, N: int) -> int:
        mod = 10 ** 9 + 7
        last = [(0, 0), (1, 0)]
        for _ in range(N):
            curr = (last[0][0] + last[0][1] + last[1][0], last[1][0] * 2 + last[1][1])
            last[0], last[1] = last[1], curr
        return last[1][0] % mod
