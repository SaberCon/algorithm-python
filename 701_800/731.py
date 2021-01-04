class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        for s, e in self.calendar:
            if start < e and end > s:
                self.overlaps.append((max(s, start), min(e, end)))
        self.calendar.append((start, end))
        return True
