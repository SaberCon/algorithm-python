class Solution:

    def findMinStep(self, board: str, hand: str) -> int:
        cache = {}
        ball_in_hand = {}
        for ball in hand:
            ball_in_hand[ball] = ball_in_hand.get(ball, 0) + 1

        def find_min_step(board):
            if board in cache:
                return cache[board]
            simplified_board = remove_group(board)
            if not simplified_board:
                return 0
            min_step = len(hand) + 1
            for ball, count in ball_in_hand.items():
                if not count:
                    continue
                ball_in_hand[ball] -= 1
                for i in range(len(simplified_board)):
                    min_step = min(min_step, find_min_step(simplified_board[:i] + ball + simplified_board[i:]) + 1)
                ball_in_hand[ball] += 1
            cache[board] = min_step
            return min_step

        def remove_group(board):
            stack = []
            for ball in board + 'E':
                if len(stack) > 2 and ball != stack[-1] and stack[-1] == stack[-2] == stack[-3]:
                    removed = stack[-1]
                    while stack and stack[-1] == removed:
                        stack.pop()
                stack.append(ball)
            stack.pop()
            return ''.join(stack)

        min_step = find_min_step(board)
        return min_step if min_step <= len(hand) else -1


print(Solution().findMinStep('WWRRBBWW', 'WRBRW'))  # 2
print(Solution().findMinStep('RRWWRRBBRR', 'WB'))  # 2
print(Solution().findMinStep('RBYYBBRRB', 'YRBGB'))  # 3
