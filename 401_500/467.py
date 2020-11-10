class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        def get_ord(char, distance):
            return (ord(char) - ord('a') + distance) % 26

        p += 'E'
        counts = [0] * 26
        start = 0
        for i in range(0, len(p)):
            if get_ord(p[start], i - start) == get_ord(p[i], 0):
                continue
            for j in range(0, min(26, i - start)):
                index = get_ord(p[start], j)
                counts[index] = max(counts[index], i - start - j)
            start = i
        return sum(counts)
