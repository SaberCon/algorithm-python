class StockSpanner:

    def __init__(self):
        self.stack = [(0, 100001)]

    def next(self, price: int) -> int:
        count = self.stack[-1][0] + 1
        while self.stack[-1][1] <= price:
            self.stack.pop()
        self.stack.append((count, price))
        return count - self.stack[-2][0]
