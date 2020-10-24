class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        is_new_word = True
        for c in s:
            if c != ' ' and is_new_word:
                ans += 1
                is_new_word = False
            if c == ' ':
                is_new_word = True
        return ans
