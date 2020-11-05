class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        for cookie in s:
            if cookie < g[ans]:
                continue
            ans += 1
            if ans == len(g):
                break
        return ans
