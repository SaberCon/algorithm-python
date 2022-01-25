class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        stack = [0]
        for start, end in clips:
            if start > stack[-1]:
                return -1
            if len(stack) > 1 and stack[-2] >= start and stack[-1] < end:
                stack.pop()
            if stack[-1] < end:
                stack.append(end)
            if end >= time:
                return len(stack) - 1
        return -1
