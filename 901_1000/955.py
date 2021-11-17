class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        indices = list(range(len(strs) - 1))
        for i in range(len(strs[0])):
            if any(strs[j][i] > strs[j + 1][i] for j in indices):
                ans += 1
                continue
            indices = [j for j in indices if strs[j][i] == strs[j + 1][i]]
        return ans
