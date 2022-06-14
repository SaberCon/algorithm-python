class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.combination = characters[:combinationLength]

    def next(self) -> str:
        current = self.combination
        for i in range(1, len(current) + 1):
            if current[-i] != self.chars[-i]:
                n = self.chars.index(current[-i])
                self.combination = current[:-i] + self.chars[n + 1:n + 1 + i]
                break
        else:
            self.combination = None
        return current

    def hasNext(self) -> bool:
        return self.combination is not None
