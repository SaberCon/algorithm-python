class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        expression = '{' + expression + '}'
        index = 0

        def parse():
            nonlocal index
            index += 1
            stack = [{''}]
            while expression[index] != '}':
                if expression[index] == ',':
                    stack.append({''})
                else:
                    words = parse() if expression[index] == '{' else {expression[index]}
                    stack.append({prefix + word for prefix in stack.pop() for word in words})
                index += 1
            return {word for s in stack for word in s}

        return sorted(parse())
