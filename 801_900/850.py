class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        event = []
        for x1, y1, x2, y2 in rectangles:
            event.append((y1, x1, x2, True))
            event.append((y2, x1, x2, False))
        event.sort()
        active = []

        def sum_x():
            total = 0
            end = 0
            for x1, x2 in active:
                total += max(0, x2 - max(end, x1))
                end = max(end, x2)
            return total

        ans = 0
        cur = event[0][0]
        for y, x1, x2, start in event:
            ans += (y - cur) * sum_x()
            cur = y
            if start:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))
        return ans % (10**9 + 7)
