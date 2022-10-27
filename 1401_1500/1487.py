from collections import defaultdict
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        name_set = set()
        name_num = defaultdict(int)
        for name in names:
            good_name = name
            while good_name in name_set:
                name_num[name] += 1
                good_name = f'{name}({name_num[name]})'
            name_set.add(good_name)
            ans.append(good_name)
        return ans
