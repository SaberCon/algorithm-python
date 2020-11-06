class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = {}
        for a in A:
            for b in B:
                AB[a + b] = AB.get(a + b, 0) + 1
        return sum(AB[-(c + d)] for d in D for c in C if -(c + d) in AB)
