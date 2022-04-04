class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = [int(s) for s in date.split('-')]
        return sum(months[:m - 1]) + d + (m > 2 and (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)))
