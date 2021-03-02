class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        return ''.join(chr(ord('a') + (ord(c) - ord('a') + shifts[i]) % 26) for i, c in enumerate(S))
