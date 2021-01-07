from collections import deque


def get_next_status(sequence):
    return (sequence[:i] + str((int(sequence[i]) + d) % 10) + sequence[i + 1:] for d in (1, -1) for i in range(4))


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append(('0000', 0))
        visited = set(deadends)
        if '0000' in visited:
            return -1
        while queue:
            sequence, count = queue.popleft()
            if sequence == target:
                return count
            for s in get_next_status(sequence):
                if s in visited:
                    continue
                visited.add(s)
                queue.append((s, count + 1))
        return -1