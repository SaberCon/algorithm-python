class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        flip_0 = [0] * (N + 1)
        flip_1 = [0] * (N + 1)
        for i in range(N):
            flip_0[i + 1] = flip_0[i] + (s[i] == '1')
            flip_1[i + 1] = flip_1[i] + (s[N - 1 - i] == '0')
        return min(flip_0[i] + flip_1[N - i] for i in range(N + 1))
