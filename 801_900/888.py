class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = sum(aliceSizes) - sum(bobSizes)
        bobSizes = set(bobSizes)
        for box in aliceSizes:
            if box - diff // 2 in bobSizes:
                return [box, box - diff // 2]