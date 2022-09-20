from collections import Counter
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        counter = Counter()
        for _, table, food in orders:
            counter[table, food] += 1
        foods = sorted(set(food for _, _, food in orders))
        tables = sorted(set(table for _, table, _ in orders), key=lambda t: int(t))
        ans = [["Table"] + foods]
        for table in tables:
            ans.append([table])
            for food in foods:
                ans[-1].append(str(counter[table, food]))
        return ans
