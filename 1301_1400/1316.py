from collections import defaultdict


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        dp = [set(range(n))]
        ans = 0
        for size in range(0, n // 2):
            _dp = []
            for indices in dp:
                index_dict = defaultdict(set)
                for i in indices:
                    if i + size < n:
                        index_dict[text[i + size]].add(i)
                for _indices in index_dict.values():
                    if any(_i + size + 1 in _indices for _i in _indices):
                        ans += 1
                    if len(_indices) > 1:
                        _dp.append(_indices)
            dp = _dp
        return ans
