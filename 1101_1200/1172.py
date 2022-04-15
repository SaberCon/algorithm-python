import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.heap = []

    def push(self, val: int) -> None:
        if self.heap:
            i = heapq.heappop(self.heap)
            if len(self.stacks) <= i:
                self.stacks.append([])
            self.stacks[i].append(val)
        else:
            if not self.stacks or len(self.stacks[-1]) == self.capacity:
                self.stacks.append([])
            self.stacks[-1].append(val)

    def pop(self) -> int:
        return self.popAtStack(len(self.stacks) - 1) if self.stacks else -1

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        heapq.heappush(self.heap, index)
        val = self.stacks[index].pop()
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return val
