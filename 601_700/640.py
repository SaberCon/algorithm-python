class Solution:
    def solveEquation(self, equation: str) -> str:
        reverse = False
        constant = x = curr = 0
        for i, c in enumerate(equation + '+'):
            if (c != '-' and c != '+' and c != '=') or curr == i:
                continue
            if equation[i - 1] == 'x':
                coefficient = equation[curr:i - 1]
                if coefficient == '' or coefficient == '+' or coefficient == '-':
                    coefficient += '1'
                x += -int(coefficient) if reverse else int(coefficient)
            else:
                constant += -int(equation[curr:i]) if reverse else int(equation[curr:i])
            if c == '=':
                reverse = True
                curr = i + 1
            else:
                curr = i
        if x == 0:
            return 'Infinite solutions' if constant == 0 else 'No solution'
        return 'x=' + str(-constant // x)
