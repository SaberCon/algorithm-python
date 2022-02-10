class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        N = len(stones)
        stones.sort()
        end = 1
        mi = N
        for i in range(N):
            while end < N and stones[end] - stones[i] + 1 <= N:
                end += 1
            if end - i == N - 1 and stones[end - 1] - stones[i] == N - 2:
                mi = min(mi, 2)
            else:
                mi = min(mi, N - (end - i))
        ma = stones[-1] - stones[0] - N + 2 - min(stones[1] - stones[0], stones[-1] - stones[-2])
        return [mi, ma]
