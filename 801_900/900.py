class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.cur = 0
        self.used = 0

    def next(self, n: int) -> int:
        while self.cur < len(self.encoding):
            if self.used + n > self.encoding[self.cur]:
                n -= self.encoding[self.cur] - self.used900
                self.cur += 2
                self.used = 0
            else:
                self.used += n
                return self.encoding[self.cur + 1]
        return -1
