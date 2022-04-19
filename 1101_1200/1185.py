class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        days = day
        days += sum(month_days[:month - 1]) + (month > 3 and year % 4 == 0 and year != 2100)
        days += 365 * (year - 1971) + (year - 1969) // 4

        return week[(days + 3) % 7]
