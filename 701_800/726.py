from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        atoms = []
        for c in formula:
            if c == '(' or c == ')' or c.isupper():
                atoms.append([c, 0])
            if c.islower():
                atoms[-1][0] += c
            if c.isdigit():
                atoms[-1][1] = 10 * atoms[-1][1] + int(c)
        stack = [Counter()]
        for atom, count in atoms:
            if count == 0:
                count = 1
            if atom == '(':
                stack.append(Counter())
            elif atom == ')':
                counter = stack.pop()
                for k in counter:
                    counter[k] *= count
                stack[-1] += counter
            else:
                stack[-1][atom] += count
        return ''.join(name + (str(count) if count > 1 else '') for name, count in sorted(stack.pop().items()))
