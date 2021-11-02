class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        down = False
        for i in range(len(arr) - 1):
            d = arr[i + 1] - arr[i]
            if d == 0 or (i == 0 and d < 0) or (down and d > 0):
                return False
            if not down and d < 0:
                down = True
        return down
