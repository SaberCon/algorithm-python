class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        indices = {}
        for i, c in enumerate(S):
            if c in indices:
                indices[c][1] = i
            else:
                indices[c] = [i, i]
        ans = []
        curr = 0
        for start, end in sorted(indices.values()):
            if start > curr:
                ans.append(curr)
            curr = max(curr, end)
        return [e - s for s, e in zip([-1] + ans, ans + [len(S) - 1])]
