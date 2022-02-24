from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return Counter((tuple(n for n in row) if row[0] else tuple(1 - n for n in row)) for row in matrix) \
            .most_common(1)[0][1]
