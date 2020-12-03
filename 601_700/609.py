class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        groups = {}
        for p in paths:
            d, *files = p.split(' ')
            for f in files:
                part = f.index('(')
                name, content = f[:part], f[part + 1:-1]
                groups.setdefault(content, [])
                groups[content].append(d + '/' + name)
        return filter(lambda g: len(g) > 1, groups.values())
