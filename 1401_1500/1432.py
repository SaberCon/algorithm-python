class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        d1 = next((d for d in num if d != '9'), '9')
        d2 = num[0] if num[0] != '1' else next((d for d in num if d not in '01'), '0')
        return int(num.replace(d1, '9')) - int(num.replace(d2, '1' if num[0] != '1' else '0'))
