class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def index(c):
            return ord(c) - ord('a')

        if len(s1) > len(s2):
            return False
        chars = [0] * 26
        for c in s1:
            chars[index(c)] += 1
        count_0 = sum(count == 0 for count in chars)
        for i, c in enumerate(s2):
            if i >= len(s1):
                chars[index(s2[i - len(s1)])] += 1
                if chars[index(s2[i - len(s1)])] == 0:
                    count_0 += 1
                if chars[index(s2[i - len(s1)])] == 1:
                    count_0 -= 1
            chars[index(c)] -= 1
            if chars[index(c)] == 0:
                count_0 += 1
            if chars[index(c)] == -1:
                count_0 -= 1
            if count_0 == 26:
                return True
        return False


Solution().checkInclusion("ab", "eidbaooo")
