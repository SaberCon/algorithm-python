from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        mid = arr[(len(arr) - 1) // 2]
        start, end = 0, len(arr) - 1
        ans = []
        for _ in range(k):
            if mid - arr[start] > arr[end] - mid:
                ans.append(arr[start])
                start += 1
            else:
                ans.append(arr[end])
                end -= 1
        return ans
