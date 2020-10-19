class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def index(char):
            return ord(char) - ord('A')

        counts = [0] * 26
        left = 0
        history_max = 0
        for right in range(len(s)):
            counts[index(s[right])] += 1
            history_max = max(history_max, counts[index(s[right])])
            if history_max + k < right - left + 1:
                counts[index(s[left])] -= 1
                left += 1
        return len(s) - left
