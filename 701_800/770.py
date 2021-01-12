class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        variables = dict(zip(evalvars, evalints))
        parts = expression.split()
        for i, part in parts:
            var = part.strip('()')
            if var in variables:
                parts[i] = part.replace(var, str(variables[var]))
