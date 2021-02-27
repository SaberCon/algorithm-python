class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i1, i2 = len(S) - 1, len(T) - 1
        skip1 = skip2 = 0
        while i1 >= 0 or i2 >= 0:
            c1 = c2 = ''
            while i1 >= 0:
                if skip1 == 0 and S[i1] != '#':
                    c1 = S[i1]
                    break
                skip1 += 1 if S[i1] == '#' else -1
                i1 -= 1
            while i2 >= 0:
                if skip2 == 0 and T[i2] != '#':
                    c2 = T[i2]
                    break
                skip2 += 1 if T[i2] == '#' else -1
                i2 -= 1
            if c1 != c2:
                return False
            i1 -= 1
            i2 -= 1
        return True
