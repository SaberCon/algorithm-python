class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if l < 2:
            return str(int(n) - 1)
        if n.count('9') == l:
            return '1' + '0' * (l - 1) + '1'
        if n[0] == '1' and (n[-1] == '1' or n[-1] == '0') and n[1:-1].count('0') == l - 2:
            return '9' * (l - 1)
        left = int(n[:(l + 1) // 2])
        near = ((s + (s[-2::-1] if l % 2 else s[::-1])) for s in (str(i) for i in range(left - 1, left + 2)))
        return min(near, key=lambda s: abs(int(s) - int(n)) if s != n else int(s) + int(n))
