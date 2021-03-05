from collections import defaultdict


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        less_richer = defaultdict(list)
        for x, y in richer:
            less_richer[x].append(y)
        ans = [-1] * len(quiet)
        for q, i in sorted((q, i) for i, q in enumerate(quiet)):
            if ans[i] >= 0:
                continue
            ans[i] = i
            stack = [i]
            while stack:
                curr = stack.pop()
                for less in less_richer[curr]:
                    if ans[less] >= 0:
                        continue
                    ans[less] = i
                    stack.append(less)
        return ans
