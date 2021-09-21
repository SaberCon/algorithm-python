from collections import Counter, defaultdict


class FreqStack:

    def __init__(self):
        self.counter = Counter()
        self.stacks = defaultdict(list)
        self.max = 0

    def push(self, val: int) -> None:
        freq = self.counter[val] + 1
        self.counter[val] = freq
        self.stacks[freq].append(val)
        self.max = max(self.max, freq)

    def pop(self) -> int:
        val = self.stacks[self.max].pop()
        self.counter[val] -= 1
        if not self.stacks[self.max]:
            self.max -= 1
        return val
