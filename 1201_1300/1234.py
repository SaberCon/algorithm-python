class Solution:
    def balancedString(self, s: str) -> int:
        s = [0 if c == 'Q' else (1 if c == 'W' else (2 if c == 'E' else 3)) for c in s]
        n, m = len(s), len(s) // 4
        times = [0] * 4
        for c in s:
            times[c] += 1
        i = 0
        ans = n
        for j, c in enumerate(s):
            times[c] -= 1
            if not all(t <= m for t in times):
                continue
            while i < n and times[s[i]] < m:
                times[s[i]] += 1
                i += 1
            ans = min(ans, j - i + 1)
        return ans
