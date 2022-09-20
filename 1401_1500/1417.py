class Solution:
    def reformat(self, s: str) -> str:
        chars1, chars2 = [c for c in s if c.isnumeric()], [c for c in s if not c.isnumeric()]
        if len(chars1) < len(chars2):
            chars1, chars2 = chars2, chars1
        if len(chars1) - len(chars2) > 1:
            return ''
        return ''.join(c1 + c2 for c1, c2 in zip(chars1, chars2)) + ('' if len(chars1) == len(chars2) else chars1[-1])
