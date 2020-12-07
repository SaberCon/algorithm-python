class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        ans = [0] * n
        for log in logs:
            id, type, timestamp = log.split(':')
            if type == 'start':
                stack.append([int(timestamp), 0])
            else:
                start_time, executed = stack.pop()
                ans[int(id)] += int(timestamp) + 1 - start_time - executed
                if stack:
                    stack[-1][1] += int(timestamp) + 1 - start_time
        return ans
