class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped = popped[::-1]
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and popped[-1] == stack[-1]:
                popped.pop()
                stack.pop()
        return not stack
