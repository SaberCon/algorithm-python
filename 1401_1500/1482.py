from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(day: int) -> bool:
            bouquets, flowers = m, k
            for b in bloomDay:
                if b <= day:
                    flowers -= 1
                    if flowers == 0:
                        bouquets -= 1
                        flowers = k
                else:
                    flowers = k
            return bouquets <= 0

        if m * k > len(bloomDay):
            return -1
        start, end = min(bloomDay), max(bloomDay)
        while start < end:
            mid = (start + end) // 2
            if check(mid):
                end = mid
            else:
                start = mid + 1
        return start
