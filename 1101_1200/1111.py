class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = [0] * len(seq)
        stack = [0]
        for i, c in enumerate(seq):
            if c == '(':
                ans[i] = 1 - stack[-1]
                stack.append(1 - stack[-1])
            if c == ')':
                ans[i] = stack.pop()
        return ans
