class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i, (a, b) in enumerate(zip(arr, arr[1:])):
            if a > b:
                return i
