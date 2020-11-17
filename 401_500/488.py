class Solution:

    def findMinStep(self, board: str, hand: str) -> int:
        cache = {}
        ball_map = {}
        for ball in hand:
            ball_map[ball] = ball_map.get(ball, 0) + 1

        def find_min_step(curr_board):
            if curr_board in cache:
                return cache[curr_board]
            simplified_board = remove_group(curr_board)
            if not simplified_board:
                return 0
            curr_min_step = len(hand) + 1
            for ball, count in ball_map.items():
                if not count:
                    continue
                ball_map[ball] -= 1
                for i in range(len(simplified_board)):
                    curr_min_step = min(curr_min_step, find_min_step(simplified_board[:i] + simplified_board[i] + simplified_board[i:]) + 1)
                ball_map[ball] += 1
            cache[curr_board] = curr_min_step
            return curr_min_step

        def remove_group(curr_board):
            stack = []
            for ball in curr_board + 'E':
                if len(stack) > 2 and ball != stack[-1] and stack[-1] == stack[-2] == stack[-3]:
                    removed = stack[-1]
                    while stack and stack[-1] == removed:
                        stack.pop()
                stack.append(ball)
            stack.pop()
            return ''.join(stack)

        min_step = find_min_step(board)
        return min_step if min_step <= len(hand) else -1


print(Solution().findMinStep('WWRRBBWW', 'WRBRW'))
