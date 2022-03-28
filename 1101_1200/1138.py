class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def get_path(c1, c2):
            if c1 == 'z' and c2 != 'z':
                return 'U' + get_path('u', c2)
            n1, n2 = ord(c1) - ord('a'), ord(c2) - ord('a')
            (i1, j1) = n1 // 5, n1 % 5
            (i2, j2) = n2 // 5, n2 % 5
            return ('L' if j1 > j2 else 'R') * abs(j1 - j2) + ('U' if i1 > i2 else 'D') * abs(i1 - i2) + '!'

        return ''.join(get_path(c1, c2) for c1, c2 in zip('a' + target, target))
