class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        if l > 0 and abs(arr[l - 1] - x) <= abs(arr[l] - x):
            l -= 1
        s, e = l, l + 1
        while e - s < k:
            if e == len(arr) or (s > 0 and abs(arr[s - 1] - x) <= abs(arr[e] - x)):
                s -= 1
            else:
                e += 1
        return arr[s:e]
