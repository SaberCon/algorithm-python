from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
        ans = []
        for size, people in groups.items():
            for i in range(0, len(people), size):
                ans.append(people[i:i + size])
        return ans
