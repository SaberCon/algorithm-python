class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p = '_' + p
        counts = [0] * 26
        length = 0
        for i in range(1, len(p)):
            index = ord(p[i]) - ord('a')
            last_index = ord(p[i - 1]) - ord('a')
            length = length + 1 if (index - last_index) % 26 == 1 else 1
            counts[index] = max(counts[index], length)
        return sum(counts)
