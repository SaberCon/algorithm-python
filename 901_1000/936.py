from collections import deque


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        M, N = len(stamp), len(target)

        todo = []
        queue = deque()
        seen = [False] * N
        ans = []

        def add_move_if_possible(i):
            if todo[i]:
                return
            ans.append(i)
            for j in range(i, i + M):
                if not seen[j]:
                    queue.append(j)
                    seen[j] = True

        for i in range(N - M + 1):
            todo.append(set(i + j for j in range(M) if stamp[j] != target[i + j]))
            add_move_if_possible(i)

        while queue:
            i = queue.popleft()

            for j in range(max(0, i - M + 1), min(N - M, i) + 1):
                if i in todo[j]:
                    todo[j].discard(i)
                    add_move_if_possible(j)

        return ans[::-1] if all(seen) else []
