from collections import Counter


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        ans = 0
        for counts in (Counter(map(tuple, board)), Counter(zip(*board))):
            if len(counts) != 2 or sorted(counts.values()) != [n // 2, (n + 1) // 2]:
                return -1
            line1, line2 = counts
            if not all(i ^ j for i, j in zip(line1, line2)):
                return -1
            if n % 2:
                first = 0 if line1.count(0) > n // 2 else 1
                ans += sum(i ^ j for i, j in zip(line1, [first, 1 - first] * (n // 2 + 1))) // 2
            else:
                ans += min(sum(i ^ j for i, j in zip(line1, match)) for match in
                           ([1, 0] * (n // 2), [0, 1] * (n // 2))) // 2
        return ans
