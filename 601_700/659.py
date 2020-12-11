from collections import defaultdict


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        seqs = defaultdict(list)
        for num in nums:
            if seqs[num - 1]:
                seqs[num].insert(0, seqs[num - 1].pop() + 1)
            else:
                seqs[num].append(1)
        return all(all(s > 2 for s in seq) for seq in seqs.values())
