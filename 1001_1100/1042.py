class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        types = {1, 2, 3, 4}
        gardens = [[] for _ in range(n)]
        for x, y in paths:
            gardens[max(x, y) - 1].append(min(x, y) - 1)
        ans = [0] * n
        for i in range(n):
            ans[i] = (types - {ans[g] for g in gardens[i]}).pop()
        return ans
