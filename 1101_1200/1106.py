class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        index = 0

        def parse():
            nonlocal index
            c = expression[index]
            if c == 't' or c == 'f':
                index += 1
                return True if c == 't' else False
            if c == '!':
                index += 2
                b = parse()
                index += 1
                return not b
            index += 1
            bs = []
            while expression[index] != ')':
                index += 1
                bs.append(parse())
            index += 1
            return all(bs) if c == '&' else any(bs)

        return parse()
