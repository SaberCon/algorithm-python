class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def to_count(word):
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            return count

        min_count = [100] * 26
        for word in words:
            count = to_count(word)
            for i, c in enumerate(count):
                min_count[i] = min(min_count[i], c)

        ans = []
        for i, c in enumerate(min_count):
            ans.extend([chr(i + ord('a'))] * c)
        return ans
