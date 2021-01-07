from collections import defaultdict


class Solution:
    def evaluate(self, expression: str) -> int:
        variables = defaultdict(list)
        args = expression.split(' ')
        args.reverse()

        def calc_value():
            curr = args.pop().rstrip(')')
            if curr.isdigit() or curr[0] == '-':
                return int(curr)
            if curr.isalnum():
                return variables[curr][-1]
            if curr == '(add':
                return calc_value() + calc_value()
            if curr == '(mult':
                return calc_value() * calc_value()
            curr_variables = []
            while args[-1].isalnum():
                curr_variables.append(args.pop())
                variables[curr_variables[-1]].append(calc_value())
            ans = calc_value()
            for var in curr_variables:
                variables[var].pop()
            return ans

        return calc_value()
