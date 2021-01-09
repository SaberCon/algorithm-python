from functools import cmp_to_key


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        if len(S) < 6:
            return S
        start = count = 0
        parts = []
        for i, c in enumerate(S):
            if c == '0':
                count -= 1
            if c == '1':
                count += 1
            if count == 0:
                if start == 0 and i == len(S) - 1:
                    break
                parts.append(self.makeLargestSpecial(S[start:i + 1]))
                start = i + 1
        if not parts:
            return '1' + self.makeLargestSpecial(S[1:-1]) + '0'
        parts.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
        return ''.join(parts)
