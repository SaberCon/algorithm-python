import heapq
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full_lakes = {}
        dry_days, dry_actions = [], []
        for day, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(day)
                continue
            if lake in full_lakes:
                dry_actions.append((full_lakes[lake], day, lake))
            full_lakes[lake] = day
        dry_actions.sort(reverse=True)

        heap = []
        ans = [-1] * len(rains)
        for day in dry_days:
            while dry_actions and dry_actions[-1][0] < day:
                start, end, lake = dry_actions.pop()
                heapq.heappush(heap, (end, lake))
            if heap:
                end, lake = heapq.heappop(heap)
                if end < day:
                    return []
                ans[day] = lake
            else:
                ans[day] = 1
        return ans if not dry_actions and not heap else []
