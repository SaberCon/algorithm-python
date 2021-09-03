class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        peak, size = max(piles), len(piles)
        top = (peak + h // size - 1) // (h // size)
        bot = (peak + h - size) // (h - size + 1)
        while bot < top:
            mid = (bot + top) // 2
            if sum((p + mid - 1) // mid for p in piles) > h:
                bot = mid + 1
            else:
                top = mid
        return bot
