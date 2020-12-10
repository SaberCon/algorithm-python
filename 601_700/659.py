class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        seqs = []
        for num in nums + [nums[-1] + 2]:
            used = False
            for s in reversed(seqs):
                if num == s[-1] + 1:
                    s.append(num)
                    used = True
                    break
                if num > s[-1] + 1:
                    break
            if not used:
                seqs.append([num])
        return all(len(s) > 2 for s in seqs)
