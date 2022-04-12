class Solution:
    def lastSubstring(self, s: str) -> str:
        N = len(s)
        i, j = 0, 1
        while j < N:
            for k in range(N):
                if j + k == N or s[j + k] < s[i + k]:
                    j += k + 1
                    break
                if s[j + k] > s[i + k]:
                    i = max(j, j + k - k % (j - i))
                    j = i + 1
                    break
        return s[i:]
