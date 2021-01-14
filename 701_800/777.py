class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start = [(c, i) for i, c in enumerate(start) if c != 'X']
        end = [(c, i) for i, c in enumerate(end) if c != 'X']
        if len(start) != len(end):
            return False
        for (sc, si), (ec, ei) in zip(start, end):
            if sc != ec:
                return False
            if sc == 'L' and si < ei:
                return False
            if sc == 'R' and si > ei:
                return False
        return True
