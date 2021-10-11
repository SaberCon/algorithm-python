class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count_char(word):
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            return count

        chars = [0] * 26
        for word in words2:
            count = count_char(word)
            for i in range(26):
                chars[i] = max(chars[i], count[i])

        return [word for word in words1 if all(c1 >= c2 for c1, c2 in zip(count_char(word), chars))]
