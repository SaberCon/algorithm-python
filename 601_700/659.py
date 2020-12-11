from collections import defaultdict


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts, ends = defaultdict(lambda: 0), defaultdict(lambda: 0)
        for num in nums:
            counts[num] += 1
        for num in nums:
            if not counts[num]:
                continue
            counts[num] -= 1
            if ends[num - 1]:
                ends[num - 1] -= 1
                ends[num] += 1
            else:
                if not counts[num + 1] or not counts[num + 2]:
                    return False
                counts[num + 1] -= 1
                counts[num + 2] -= 1
                ends[num + 2] += 1
        return True
