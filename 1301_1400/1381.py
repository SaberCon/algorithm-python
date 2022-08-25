class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.inc = [0]

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        inc = self.inc.pop()
        ans = self.stack.pop() + inc
        self.inc[-1] += inc
        return ans

    def increment(self, k: int, val: int) -> None:
        self.inc[min(k, len(self.stack))] += val
