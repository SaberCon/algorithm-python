class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set(int(s[i:i + k], 2) for i in range(len(s) - k + 1))) == 2 ** k
