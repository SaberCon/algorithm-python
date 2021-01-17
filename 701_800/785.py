class Solution:
    def isBipartite(self, graph: [[int]]) -> bool:
        sets = [set(), set()]
        stack = []
        for i, targets in enumerate(graph):
            if i in sets[0] or i in sets[1]:
                continue
            stack.append((i, 0))
            sets[0].add(i)
            while stack:
                index, set_index = stack.pop()
                for target in graph[index]:
                    if target in sets[set_index]:
                        return False
                    if target not in sets[1 - set_index]:
                        sets[1 - set_index].add(target)
                        stack.append((target, 1 - set_index))
        return True
