from random import randrange


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.n = N - len(blacklist)
        self.black_map = {}
        black_set = {n for n in blacklist if n >= self.n}
        curr = self.n
        for n in blacklist:
            if n >= self.n:
                continue
            while curr in black_set:
                curr += 1
            self.black_map[n] = curr
            curr += 1

    def pick(self) -> int:
        rand = randrange(0, self.n)
        if rand in self.black_map:
            return self.black_map[rand]
        return rand
