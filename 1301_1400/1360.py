import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1, date2 = datetime.date.fromisoformat(date1), datetime.date.fromisoformat(date2)
        return abs(date1 - date2).days
