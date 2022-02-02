from collections import deque


class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = deque(maxlen=max(len(word) for word in words))
        self.trie = [None] * 27
        for word in words:
            trie = self.trie
            for letter in reversed(word):
                i = ord(letter) - ord('a')
                if not trie[i]:
                    trie[i] = [None] * 27
                trie = trie[i]
            trie[26] = True

    def query(self, letter: str) -> bool:
        self.letters.appendleft(letter)
        trie = self.trie
        for letter in self.letters:
            i = ord(letter) - ord('a')
            if not trie[i]:
                return False
            trie = trie[i]
            if trie[26]:
                return True
        return False
