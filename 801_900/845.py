class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans = up = down = 0
        for curr, last in zip(arr[1:], arr):
            if curr == last or (curr > last and down > 0):
                up = down = 0
            if curr > last:
                up += 1
            if curr < last and up > 0:
                down += 1
            if up > 0 and down > 0:
                ans = max(ans, up + down + 1)
        return ans
