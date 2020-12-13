class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        s, e = 1, m * n
        while s < e:
            mid = (s + e) // 2
            if sum(min(mid // i, n) for i in range(1, m + 1)) < k:
                s = mid + 1
            else:
                e = mid
        return s
