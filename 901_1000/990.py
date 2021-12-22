class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = [i for i in range(26)]

        def union_find(i):
            return i if uf[i] == i else union_find(uf[i])

        index = lambda c: ord(c) - ord('a')

        for equation in equations:
            if equation[1:3] == '==':
                left, right = index(equation[0]), index(equation[-1])
                uf[union_find(left)] = union_find(right)

        for equation in equations:
            if equation[1:3] == '!=' and union_find(index(equation[0])) == union_find(index(equation[-1])):
                return False
        return True
