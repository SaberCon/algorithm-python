from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(lambda: 0)
        for i in range(1, n + 1):
            groups[sum(int(d) for d in str(i))] += 1
        return list(groups.values()).count(max(groups.values()))
