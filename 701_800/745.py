class Trie:

    def __init__(self):
        self.nodes = {}
        self.indices = []

    def addIndex(self, index: int):
        self.indices.append(index)

    def addWord(self, word: str, curr: int, index: int):
        if curr >= len(word):
            return
        if word[curr] not in self.nodes:
            self.nodes[word[curr]] = Trie()
        self.nodes[word[curr]].addIndex(index)
        self.nodes[word[curr]].addWord(word, curr + 1, index)

    def searchIndices(self, prefix: str, curr: int) -> [int]:
        if curr >= len(prefix):
            return self.indices
        if prefix[curr] not in self.nodes:
            return []
        return self.nodes[prefix[curr]].searchIndices(prefix, curr + 1)


class WordFilter:

    def __init__(self, words: List[str]):
        self.pre_tire = Trie()
        self.suf_tire = Trie()
        for i, word in enumerate(words):
            self.pre_tire.addWord(word, 0, i)
            self.suf_tire.addWord(word[::-1], 0, i)

    def f(self, prefix: str, suffix: str) -> int:
        pre_indices = self.pre_tire.searchIndices(prefix, 0)
        suf_indices = self.suf_tire.searchIndices(suffix[::-1], 0)
        pre_curr = len(pre_indices) - 1
        suf_curr = len(suf_indices) - 1
        while pre_curr >= 0 and suf_curr >= 0:
            if pre_indices[pre_curr] == suf_indices[suf_curr]:
                return pre_indices[pre_curr]
            if pre_indices[pre_curr] > suf_indices[suf_curr]:
                pre_curr -= 1
            else:
                suf_curr -= 1
        return -1
