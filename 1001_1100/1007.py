class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)
        count, top_count, bot_count = [0] * 7, [0] * 7, [0] * 7
        for t, b in zip(tops, bottoms):
            top_count[t] += 1
            bot_count[b] += 1
            for i in {t, b}:
                count[i] += 1
        for c, tc, bc in zip(count, top_count, bot_count):
            if c < N:
                continue
            return N - max(tc, bc)
        return -1
