from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {n: i + 1 for i, n in enumerate(sorted(set(arr)))}
        return [ranks[n] for n in arr]
