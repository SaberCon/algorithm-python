class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(' ')
        trie = [None] * 27
        for word in dictionary:
            curr = trie
            for c in word:
                i = ord(c) - ord('a')
                if not curr[i]:
                    curr[i] = [None] * 27
                curr = curr[i]
            curr[26] = True
        for i, word in enumerate(words):
            curr = trie
            for j, c in enumerate(word):
                k = ord(c) - ord('a')
                if not curr[k]:
                    break
                if curr[k][26]:
                    words[i] = word[:j + 1]
                    break
                curr = curr[k]
        return ' '.join(words)
