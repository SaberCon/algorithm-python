class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle, minute_angle = hour % 12 * 30 + minutes / 2, minutes * 6
        angle = abs(hour_angle - minute_angle)
        return min(angle, 360 - angle)
