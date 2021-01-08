from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_tops = defaultdict(list)
        for a in allowed:
            allowed_tops[a[:2]].append(a[-1])

        def can_be_built(b):
            if len(b) == 1:
                return len(b[0]) > 0
            return can_be_built([{a for l in b[i] for r in b[i + 1] for a in allowed_tops[l + r]} for i in range(len(b) - 1)])

        return can_be_built([[c] for c in bottom])
