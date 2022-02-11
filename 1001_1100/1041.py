class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        current = 0
        moves = [0] * 4
        for i in instructions:
            if i == 'G':
                moves[current] += 1
            if i == 'L':
                current = (current - 1) % 4
            if i == 'R':
                current = (current + 1) % 4
        return current != 0 or (moves[0] == moves[2] and moves[1] == moves[3])
