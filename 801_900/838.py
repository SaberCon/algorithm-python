class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        pushes = [0] * len(dominoes)
        right_push = 0
        for i, c in enumerate(dominoes):
            if c == 'R':
                right_push = 1
            elif c == 'L':
                right_push = 0
                for j in range(i - 1, -1, -1):
                    if dominoes[j] == 'L' or dominoes[j] == 'R':
                        break
                    if pushes[j] == 0 or pushes[j] > i - j:
                        pushes[j] = j - i
                    if pushes[j] == i - j:
                        pushes[j] = 0
            elif right_push > 0:
                pushes[i] = right_push
                right_push += 1
        return ''.join(c if pushes[i] == 0 else 'R' if pushes[i] > 0 else 'L' for i, c in enumerate(dominoes))
