from collections import defaultdict


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = set()
        self.md = defaultdict(lambda: 0)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                self.md[word[:i] + 'X' + word[i + 1:]] += 1
            self.d.add(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            search = self.md[searchWord[:i] + 'X' + searchWord[i + 1:]]
            if search > 1:
                return True
            if search == 1 and searchWord not in self.d:
                return True
        return False
