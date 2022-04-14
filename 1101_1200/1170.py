class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str):
            return s.count(min(s))

        frequencies = [0] * 11
        for w in words:
            frequencies[f(w) - 1] += 1
        for i in range(10, 0, -1):
            frequencies[i - 1] += frequencies[i]
        return [frequencies[f(q)] for q in queries]
