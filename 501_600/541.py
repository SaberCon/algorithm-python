class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = []
        for i, c in enumerate(s):
            if i % k == 0:
                chars.append("")
            if (i // k) % 2 == 0:
                chars[-1] = c + chars[-1]
            else:
                chars[-1] += c
        return ''.join(chars)
