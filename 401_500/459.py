class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return 0 < (s + s).find(s, 1) < len(s)
