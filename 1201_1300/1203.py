from collections import defaultdict
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        for i, g in enumerate(group):
            if g == -1:
                group[i] = m
                m += 1
            groups[group[i]].append(i)

        before_groups = [set() for _ in range(m)]
        before_items_in_groups = [defaultdict(set) for _ in range(m)]
        for i, items in enumerate(beforeItems):
            for j in items:
                if group[i] == group[j]:
                    before_items_in_groups[group[i]][i].add(j)
                else:
                    before_groups[group[i]].add(group[j])

        ans = []
        seen_groups = set()
        current_groups = set()
        seen_items = set()
        current_items = set()

        def dfs_group(g: int) -> bool:
            if g in current_groups:
                return False
            if g in seen_groups:
                return True
            current_groups.add(g)
            for bg in before_groups[g]:
                if not dfs_group(bg):
                    return False
            current_groups.remove(g)
            seen_groups.add(g)
            return all(dfs_item(g, i) for i in groups[g])

        def dfs_item(g: int, i: int) -> bool:
            if i in current_items:
                return False
            if i in seen_items:
                return True
            current_items.add(i)
            for bi in before_items_in_groups[g][i]:
                if not dfs_item(g, bi):
                    return False
            current_items.remove(i)
            seen_items.add(i)
            ans.append(i)
            return True

        return ans if all(dfs_group(g) for g in range(m)) else []
