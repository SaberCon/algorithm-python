class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        top = ans = 0
        for i, num in enumerate(arr):
            top = max(top, num)
            if top <= i:
                ans += 1
        return ans
