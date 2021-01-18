class Solution:
    def customSortString(self, S: str, T: str) -> str:
        order = {c: i for i, c in enumerate(S)}
        return ''.join(sorted(T, key=lambda c: order[c] if c in order else 0))
