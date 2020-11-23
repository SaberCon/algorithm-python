class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def is_sub(s1, s2):
            index = 0
            for c in s2:
                if index >= len(s1):
                    break
                if c == s1[index]:
                    index += 1
            return index >= len(s1)

        d.sort(key=lambda word: (-len(word), word))
        for word in d:
            if is_sub(word, s):
                return word
        return ""
