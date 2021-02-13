class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = [[0, 0]]
        last = s[0]
        for i, c in enumerate(s):
            if c == last:
                continue
            last = c
            ans[-1][1] = i - 1
            ans.append([i, i])
        ans[-1][1] = len(s) - 1
        return [p for p in ans if p[1] - p[0] > 2]
