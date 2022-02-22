from collections import Counter
from itertools import chain


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        N = len(barcodes)
        counts = sorted((c, b) for b, c in Counter(barcodes).items())
        ans = [0] * N
        for i in chain(range(0, N, 2), range(1, N, 2)):
            c, b = counts[-1]
            ans[i] = b
            if c == 1:
                counts.pop()
            else:
                counts[-1] = (c - 1, b)
        return ans
