class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_minute(s):
            hour, minute = s.split(':')
            return int(hour) * 60 + int(minute)

        minutes = sorted(map(to_minute, timePoints))
        return min(min(t1 - t2 for t1, t2 in zip(minutes[1:], minutes)), minutes[0] + 1440 - minutes[-1])
