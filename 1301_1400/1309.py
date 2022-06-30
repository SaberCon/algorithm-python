class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = []
        while i < len(s):
            c = s[i]
            if i < len(s) - 2 and s[i + 2] == '#':
                ans.append(chr(ord('a') + int(s[i:i + 2]) - 1))
                i += 3
            else:
                ans.append(chr(ord('a') + int(c) - 1))
                i += 1
        return ''.join(ans)
