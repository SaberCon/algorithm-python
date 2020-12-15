class Solution:
    def checkValidString(self, s: str) -> bool:
        p = stars = 0
        for c in s:
            if c == '*':
                stars += 1
            if c == '(':
                p += 1
            if c == ')':
                if p == 0:
                    if stars == 0:
                        return False
                    stars -= 1
                else:
                    p -= 1
        p = stars = 0
        for c in reversed(s):
            if c == '*':
                stars += 1
            if c == ')':
                p += 1
            if c == '(':
                if p == 0:
                    if stars == 0:
                        return False
                    stars -= 1
                else:
                    p -= 1
        return True
