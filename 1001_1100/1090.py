from collections import defaultdict


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        counts = defaultdict(lambda: 0)
        count = 0
        ans = 0
        for value, label in sorted(zip(values, labels), reverse=True):
            if counts[label] == useLimit:
                continue
            counts[label] += 1
            count += 1
            ans += value
            if count == numWanted:
                break
        return ans
