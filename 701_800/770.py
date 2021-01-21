from collections import Counter
from functools import reduce


class Poly(Counter):
    def __add__(self, other):
        self.update(other)
        return self

    def __sub__(self, other):
        return self + {k: -v for k, v in other.items()}

    def __mul__(self, other):
        ans = Poly()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                ans[tuple(sorted(k1 + k2))] += v1 * v2
        return ans

    def evaluate(self, evalmap):
        ans = Poly()
        for k, c in self.items():
            ans[tuple(token for token in k if token not in evalmap)] += reduce(
                lambda x, y: x * y, (evalmap[token] for token in k if token in evalmap), c)
        return ans

    def to_list(self):
        return ['*'.join((str(v),) + k) for k, v in sorted(self.items(), key=lambda kv: (-len(kv[0]), kv[0])) if v]


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        evalmap = dict(zip(evalvars, evalints))

        def combine(left, right, symbol):
            if symbol == '+': return left + right
            if symbol == '-': return left - right
            if symbol == '*': return left * right
            raise

        def make(expr):
            ans = Poly()
            if expr.isdigit():
                ans[()] = int(expr)
            else:
                ans[(expr,)] = 1
            return ans

        def parse(expr):
            bucket = []
            symbols = []
            i = 0
            while i < len(expr):
                if expr[i] == '(':
                    bal = 0
                    for j in range(i, len(expr)):
                        if expr[j] == '(': bal += 1
                        if expr[j] == ')': bal -= 1
                        if bal == 0:
                            bucket.append(parse(expr[i + 1:j]))
                            i = j
                            break
                elif expr[i].isalnum():
                    for j in range(i, len(expr) + 1):
                        if j == len(expr) or expr[j] == ' ':
                            bucket.append(make(expr[i:j]))
                            i = j
                            break
                elif expr[i] in '+-*':
                    symbols.append(expr[i])
                i += 1

            for i in range(len(symbols) - 1, -1, -1):
                if symbols[i] == '*':
                    bucket[i] = combine(bucket[i], bucket.pop(i + 1), symbols.pop(i))

            if not bucket:
                return Poly()
            ans = bucket[0]
            for i, symbol in enumerate(symbols, 1):
                ans = combine(ans, bucket[i], symbol)

            return ans

        return parse(expression).evaluate(evalmap).to_list()
