class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        stack = []
        count = 0
        for curr, prev in zip(s + 'E', 'S' + s):
            if curr != prev:
                stack.append(count)
                count = 0
            count += 1
        ans = 0
        while len(stack) > 1:
            ans += min(stack.pop(), stack[-1])
        return ans
