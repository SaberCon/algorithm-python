import collections


class Solution(object):
    def kSimilarity(self, A: str, B: str) -> int:
        def neighbors(S):
            i = next(p for p, (s, b) in enumerate(zip(S, B)) if s != b)
            return (S[:i] + S[j] + S[i + 1:j] + S[i] + S[j + 1:] for j in range(i + 1, len(S)) if S[j] == B[i])

        queue = collections.deque([(A, 0)])
        seen = {A}
        while True:
            S, count = queue.popleft()
            if S == B:
                return count
            for N in neighbors(S):
                if N not in seen:
                    seen.add(N)
                    queue.append((N, count + 1))
