from itertools import product


class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        def make_decimal(s):
            if 1 < len(s) and s.startswith('0') and s.endswith('0'):
                return []
            if s.endswith('0'):
                return [s]
            if s.startswith('0'):
                return ['0.' + s[1:]]
            return [s[:i] + '.' + s[i:] if s[i:] else s[:i] for i in range(1, len(s) + 1)]

        S = S[1:-1]
        return ['({}, {})'.format(l, r) for i in range(1, len(S))
                for l, r in product(make_decimal(S[:i]), make_decimal(S[i:]))]
