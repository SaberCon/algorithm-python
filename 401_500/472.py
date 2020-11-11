class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = {}

        def add_to_trie(word):
            curr = trie
            for c in word:
                curr.setdefault(c, {})
                curr = curr[c]
            curr['E'] = True

        def is_in_trie(word, start, end):
            if start >= end:
                return True
            curr = trie
            for i in range(start, end):
                if word[i] not in curr:
                    return False
                curr = curr[word[i]]
                if 'E' in curr and is_in_trie(word, i + 1, end):
                    return True
            return False

        words.sort(key=len)
        ans = []
        for word in words:
            if not word:
                continue
            if is_in_trie(word, 0, len(word)):
                ans.append(word)
            add_to_trie(word)
        return ans
