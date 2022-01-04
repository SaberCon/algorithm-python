class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c != 'c':
                stack.append(c)
            elif len(stack) < 2 or stack.pop() != 'b' or stack.pop() != 'a':
                return False
        return not stack
