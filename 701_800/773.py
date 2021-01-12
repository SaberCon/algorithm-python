class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        target = '123450'
        queue = [(''.join(''.join(map(str, r)) for r in board), 0)]
        seen = set()
        while queue:
            curr, count = queue.pop(0)
            if curr == target:
                return count
            seen.add(curr)
            i = curr.index('0')
            for j in moves[i]:
                chars = list(curr)
                chars[i] = chars[j]
                chars[j] = '0'
                next_state = ''.join(chars)
                if next_state not in seen:
                    queue.append((next_state, count + 1))
        return -1
