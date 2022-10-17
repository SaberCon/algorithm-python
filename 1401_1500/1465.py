from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts.extend((h, 0))
        verticalCuts.sort()
        verticalCuts.extend((w, 0))
        return max(horizontalCuts[i] - horizontalCuts[i - 1] for i in range(len(horizontalCuts) - 1)) \
            * max(verticalCuts[i] - verticalCuts[i - 1] for i in range(len(verticalCuts) - 1)) \
            % 1000000007
